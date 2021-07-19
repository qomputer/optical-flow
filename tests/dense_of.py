import os
import cv2
import numpy as np
import utils


def draw_flow(algorithm, method, video_path, params=[], to_gray=False, to_display=False, rows = []):
    cap = cv2.VideoCapture(video_path)
    ret, old_frame = cap.read()
    if rows:
        old_frame = utils.rem_pad(old_frame, rows)
    # crate HSV & make Value a constant
    hsv = np.zeros_like(old_frame)
    hsv[..., 1] = 255
    if to_gray:
        old_frame = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    filename = os.path.basename(video_path)
    (file, ext) = os.path.splitext(filename)
    out = cv2.VideoWriter(os.path.join("videos", "%s-%s.mp4" % (algorithm, file)),fourcc, 25.0, (1200, 980))
    while 1:
        ret, new_frame = cap.read()
        frame_copy = new_frame
        if not ret:
            break
        if rows:
            new_frame = utils.rem_pad(new_frame, rows)
        if to_gray:
            new_frame = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)
        # Calculate Optical Flow
        flow = method(old_frame, new_frame, *params)
        # Encoding: convert the algorithm's output into Polar coordinates
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        # Use Hue and Saturation to encode the Optical Flow
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        # Convert HSV image into BGR for demo
        bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        vert = np.concatenate((frame_copy, bgr), axis=0)
        vert = cv2.resize(vert, (1200, 980))
        if to_display:
            cv2.imshow('Two images', vert)
        else:
            out.write(vert)
            #cv2.imshow("frame", frame_copy)
            #cv2.imshow("optical flow", bgr)
        k = cv2.waitKey(25) & 0xFF
        if k == 27:
            break
        old_frame = new_frame


def drawM_flow(algorithm, method, video_path, params=[], to_gray=False, to_display=False):
    cap = cv2.VideoCapture(video_path)
    ret, old_frame = cap.read()
    # crate HSV & make Value a constant
    hsv = np.zeros_like(old_frame)
    hsv[..., 1] = 255
    if to_gray:
        old_frame = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # filename = os.path.basename(video_path)
    # (file, ext) = os.path.splitext(filename)
    # out = cv2.VideoWriter(os.path.join("videos", "%s-%s.mp4" % (algorithm, file)),fourcc, 25.0, (1200, 980))
    while True:
        ret, new_frame = cap.read()
        if not ret:
            break
        frame_copy = new_frame
        if to_gray:
            new_frame = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)
        # Calculate Optical Flow
        flow = method(old_frame, new_frame, *params)
        #flowF = cv2.calcOpticalFlowFarneback(old_frame, new_frame, None, 0.5, 2, 20, 3, 5, 1.2, 0)
        #utils.visualize_flow(flow)
        iflow = utils.flow_to_image(flow)
        vert = np.concatenate((frame_copy, iflow), axis=0)
        vert = cv2.resize(vert, (1200, 980))
        cv2.imshow('Two images', vert)
        k = cv2.waitKey(25) & 0xFF
        if k == 27:
            break
        old_frame = new_frame