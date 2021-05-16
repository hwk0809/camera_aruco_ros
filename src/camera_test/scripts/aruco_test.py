import cv2
import numpy as np
from cv2 import aruco

path='/home/alejandrocruzado/Documents/Imaginni/aruco4.png'
path_5 = '/home/alejandrocruzado/Documents/Imaginni/aruco5.jpg'
path5x5 = '/home/alejandrocruzado/Documents/Imaginni/5x5.jpg'
distCoeffs=[0.0189223469433419, -0.0206788674793396,0.003225513523750, 0.001510000668961]
cameraMatrix=[[600.8293, 0, 330.2756],[0, 601.3519, 225.9791],[0, 0, 1.0000]]

def MarkerDetection4x4(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    aruco_dict = cv2.aruco_Dictionary.get(aruco.DICT_4X4_1000)
    parameters = cv2.aruco_DetectorParameters.create()
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    cv2.aruco.drawDetectedMarkers(img,corners,ids,)
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    rvecs, tvecs, _objPoints = cv2.aruco.estimatePoseSingleMarkers(corners, 0.045, cameraMatrix, distCoeffs)
    cv2.aruco.drawAxis(img, cameraMatrix, distCoeff, rvecs, tvecs, 0.1)


def MarkerDetection5x5(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    aruco_dict = cv2.aruco_Dictionary.get(aruco.DICT_5X5_250)
    parameters = cv2.aruco_DetectorParameters.create()
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    cv2.aruco.drawDetectedMarkers(img,corners,ids,)
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    rvecs, tvecs, _objPoints = cv2.aruco.estimatePoseSingleMarkers(corners, 0.045, cameraMatrix, distCoeffs)
    cv2.aruco.drawAxis(img, cameraMatrix, distCoeff, rvecs, tvecs, 0.1)


if __name__ == "__main__":

    #MarkerDetection4x4(path)
    MarkerDetection5x5(path5x5)