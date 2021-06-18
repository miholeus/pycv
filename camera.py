import cv2


class Mirror:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)

    def read(self):
        ret, frame = self.cam.read()
        return cv2.flip(frame, 1)

    def update(self):
        cv2.imshow('frame', self.read())

    def release(self):
        self.cam.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    mirror = Mirror()
    while True:
        mirror.update()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    mirror.release()
