import itertools
import cv2

vid = cv2.VideoCapture(0) 

width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('outrecorded.avi',fourcc,24,(int(width),int(height)))

a = 1
while(vid.isOpened()):
    ret, frame = vid.read()
    if ret:
        out.write(frame)
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # plt.axis('off')
        # plt.title('stream')
        # plt.imshow(frame)
        # plt.show
        cv2.imshow('image',frame)
        cv2.waitKey(25)
        # cv2.destroyAllWindows()
#         break
    else:
        break
vid.release()
out.release()