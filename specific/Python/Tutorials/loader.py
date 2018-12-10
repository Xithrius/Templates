def loader(times, M=2.4, m=0.12):
    bar = progressbar.ProgressBar()
    for i in bar(range(times)):
        x = random.random()

        step = (M - m) * x + m

        time.sleep(step)


def fixedTimeLoader(t, minStepSize=0.1, maxStepSize=1):
    timeSteps = []

    while t >= minStepSize:
        r = random.random() * (maxStepSize - minStepSize) + minStepSize

        if r > t:
            r = t

        timeSteps.append(r)
        t -= r

    if t != 0:
        timeSteps.append(t)

    bar = progressbar.ProgressBar()
    for i in bar(timeSteps):
        time.sleep(i)


fixedTimeLoader(2, 0.1, 0.5)
