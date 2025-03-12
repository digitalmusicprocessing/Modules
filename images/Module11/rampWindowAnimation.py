import numpy as np
import matplotlib.pyplot as plt

def plotPosNeg(s):
    idxn = np.arange(len(s))
    sn = s[s < 0]
    idxn = idxn[s < 0]
    sp = s[s >= 0]
    idxp = np.arange(len(s))
    idxp = idxp[s >= 0]
    if len(idxp) > 0:
        plt.stem(idxp, sp, 'r', markerfmt='ro')
    if len(idxn) > 0:
        plt.stem(idxn, sn, 'b')

if __name__ == '__main__2':
    N = 31
    for i in range(N):
        f = np.floor((i+1)/2)
        plt.subplot(6, 6, i)
        y = np.cos(np.arange(N)*2*np.pi*f/N)
        if i%2 == 0:
            y = np.sin(np.arange(N)*2*np.pi*f/N)
        plt.plot(y)
        plt.axis('off')
    plt.show()

if __name__ == '__main__':
    N = 1001
    #x = np.exp(-(np.array(np.arange(N), dtype=np.int64)-150.0)**2/(10.0**2))
    a0 = 0.21557895
    a1 = 0.41663158
    a2 = 0.277263158
    a3 = 0.083578947
    a4 = 0.006947368
    t = 2*np.pi*np.arange(N)/N
    w = 1#np.sin(0.5*t)#a0 - a1*np.cos(t) + a2*np.cos(2*t) - a3 * np.cos(3*t) + a4*np.cos(4*t)
    fac = 1
    plt.figure(figsize=(fac*8, fac*10))
    plot_lim = 10
    rg = 1.1
    xticks = np.arange(0, plot_lim+1)
    for shift in range(1, N):
        x = np.cos(3.3*t)

        """
        x = (2*np.arange(N)) % N
        x = np.array(x, dtype=float)
        x -= N/2
        x = x/np.max(x)
        """

        x = x*w
        y = 0*x
        y[0:shift] = x[-shift:]
        y[shift:] = x[0:-shift]
        sines = np.zeros(N//2)
        cosines = np.zeros(N//2)
        for i in range(N//2):
            cosines[i] = np.sum(y*np.cos(np.arange(N)*2*np.pi*i/N))/(N/2)
            sines[i] = np.sum(y*np.sin(-np.arange(N)*2*np.pi*i/N))/(N/2)
        
        z = np.concatenate((y, y, y))
        
        lw = 2
        plt.clf()
        plt.subplot2grid((3, 2), (0, 0), colspan=2, rowspan=1)
        plt.plot(z, antialiased=True, linewidth=lw)
        z[0:N] = 0
        z[-N:] = 0
        plt.plot(z, antialiased=True, linewidth=lw)
        plt.plot([N, N], [0, 1.0], 'C1', antialiased=True, linewidth=lw)
        plt.plot([2*N, 2*N], [0, 1.0], 'C1', antialiased=True, linewidth=lw)
        plt.title('Shifting A 3.3 Cycles Per Window Sinusoid')

        plt.subplot(323)
        plt.stem(cosines)
        plt.ylim([-rg, rg])
        plt.xlim([-0.5, plot_lim+0.5])
        plt.xticks(xticks)
        plt.title('Cosine Projections')
        plt.xlabel("Frequency Index")
        plt.ylabel("Projection")

        plt.subplot(324)
        plt.stem(sines)
        plt.ylim([-rg, rg])
        plt.xlim([-0.5, plot_lim+0.5])
        plt.xticks(xticks)
        plt.title('Sine Projections')
        plt.xlabel("Frequency Index")
        plt.ylabel("Projection")

        plt.subplot(325)
        amps = np.sqrt(np.array(sines)**2 + np.array(cosines)**2)
        phases = np.arctan2(sines, cosines)
        phases[amps < 1e-3] = 0
        plt.stem(amps)
        plt.xlim([-0.5, plot_lim+0.5])
        plt.ylim([-0.1, rg])
        plt.xticks(xticks)
        
        #yticks = (2/np.pi)*(1/np.arange(1, 5))
        #plt.grid(axis='y', linestyle='--')
        #plt.yticks(yticks, [f"$(2/\\pi)$/{i}" for i in range(1, len(yticks)+1)])

        
        
        plt.title('Amplitude')
        plt.xlabel("Frequency Index")
        plt.ylabel("Amplitude")
        plt.tight_layout()

        plt.subplot(326)
        plt.stem((amps > 3e-2)*phases)
        plt.ylim([-np.pi-0.1, np.pi+0.1])
        plt.xlim([-0.5, plot_lim+0.5])
        plt.xticks(xticks)
        plt.yticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], ["$-\\pi$", "$\\pi/2$", "0", "$\\pi/2$", "$\\pi$"])
        plt.xlabel("Frequency Index")
        plt.ylabel("Phase (Radians)")
        plt.title("Phase")

        plt.savefig("Sinusoid3Point3%i.png"%shift, dpi = 120, bbox_inches='tight')

