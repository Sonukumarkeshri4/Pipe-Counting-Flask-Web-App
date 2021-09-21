import cv2
import numpy as np

'''
def MyImage():
    img = cv2.imread("pipes2.jpg")
    #cv2.imshow('original',img)
    cv2.waitKey()
    return img
'''

def circleDetection(imagePath):
    image = cv2.imread(imagePath)
    detector = cv2.SimpleBlobDetector_create()

    keypoints = detector.detect(image)

    blank = np.zeros((1,1))
    blobs = cv2.drawKeypoints(image,keypoints,blank,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    number_of_blobs = len(keypoints)

    text = "total number of pipes:" + str(len(keypoints))

    cv2.putText(blobs, text, (20,550), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    #cv2.imshow('blobs using default parameters',blobs)
    #cv2.waitKey()

    params = cv2.SimpleBlobDetector_Params()

    params.minThreshold = 10;

    params.maxThreshold = 200;
    params.filterByArea = True
    params.minArea =400

    params.filterByCircularity = True

    params.minCircularity = 0.1
    params.filterByConvexity = True
    params.minConvexity = 0.8

    params.filterByInertia = True
    params.minInertiaRatio = 0.01


    detector = cv2.SimpleBlobDetector_create(params)

    keypoints = detector.detect(image)
    blank = np.zeros((1,1))
    blobs = cv2.drawKeypoints(image,keypoints,blank,(0,255,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    number_of_blobs = len(keypoints)

    text = "number of pipes:" + str(len(keypoints))
    print(text)
    cv2.putText(blobs, text, (5,40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    cv2.putText(blobs, text, (6, 82), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(blobs, text, (6, 124), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

    #cv2.imshow('filtering circular blobs only',blobs)
    cv2.waitKey()

    cv2.destroyAllWindows()
    return blobs



'''
def rectDetection(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
    # Find Canny edges
    edged = cv2.Canny(gray, 10, 35)
    cv2.waitKey(0)
      
    cv2.imshow('Canny Edges After Contouring', edged)
    cv2.waitKey(0)
    
          
        


    
def main():
    image=MyImage()
    circles = circleDetection(image)
    #rectDetection(image)

if __name__ == "__main__":
    main()

'''





