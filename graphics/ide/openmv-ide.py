import sensor, image, time

# Setup Camera
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(10)
threshold = (10, 90, -80, -30, 20, 50)
clock = time.clock()

# Find blobs
while(True):
    clock.tick()
    img = sensor.snapshot()
    for b in img.find_blobs([threshold]):
        img.draw_rectangle(b[0:4])
        print("====\nBlob %s" % str(b))
    print("FPS %d" % clock.fps())
