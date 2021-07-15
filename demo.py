from argparse import ArgumentParser

import cv2

from algorithms.dense_of import draw_flow
from algorithms.sparse_of import lucas_kanade_method

def main():
    parser = ArgumentParser()
    parser.add_argument(
        "--algorithm",
        choices=["farneback", "lucaskanade", "lucaskanade_dense", "rlof", "dis", "deepflow", "tvl1", "sf", "pca"],
        required=True,
        help="Optical flow algorithm to use",
    )
    parser.add_argument(
        "--video_path", default="videos/cat.mp4", help="Path to the video",
    )

    args = parser.parse_args()
    video_path = args.video_path
    if args.algorithm == "lucaskanade":
        lucas_kanade_method(video_path)
    elif args.algorithm == "lucaskanade_dense":
        method = cv2.optflow.calcOpticalFlowSparseToDense
        params = [None]
        draw_flow(args.algorithm, method, video_path, params, to_gray=True)
    elif args.algorithm == "rlof":
        method = cv2.optflow.calcOpticalFlowDenseRLOF
        params = [None]
        draw_flow(args.algorithm,method, video_path, params)
    elif args.algorithm == "deepflow":
        method = cv2.optflow.createOptFlow_DeepFlow()
        params = [None]
        draw_flow(args.algorithm, method.calc, video_path, params, to_gray=True)
    elif args.algorithm == "sf":
        method = cv2.optflow.calcOpticalFlowSF
        params = [5, 2, 4]                         # [layers, ]
        draw_flow(args.algorithm, method, video_path, params, to_gray=False)
    elif args.algorithm == "pca":
        method = cv2.optflow.createOptFlow_PCAFlow()
        params = [None]
        draw_flow(args.algorithm, method.calc, video_path, params, to_gray=True)
# The best methods
    elif args.algorithm == "tvl1":
        params = [None]
        method = cv2.optflow.DualTVL1OpticalFlow_create(nscales=2,epsilon=0.05,warps=2)
        draw_flow(args.algorithm, method.calc, video_path, params, to_gray=True)
    elif args.algorithm == "dis":
        params = [None]
        method = cv2.DISOpticalFlow_create(cv2.DISOPTICAL_FLOW_PRESET_MEDIUM)
        draw_flow(args.algorithm, method.calc, video_path, params, to_gray=True)#
    elif args.algorithm == "farneback":
        method = cv2.calcOpticalFlowFarneback
        params = [None, 0.5, 2, 20, 3, 5, 1.2, 0]  #  pyr_scale=0.5, levels=2, winsize=80, iterations=2, poly_n=7, poly_sigma=4.5, flags=0
        draw_flow(args.algorithm, method, video_path, params, to_gray=True)


if __name__ == "__main__":
    main()
