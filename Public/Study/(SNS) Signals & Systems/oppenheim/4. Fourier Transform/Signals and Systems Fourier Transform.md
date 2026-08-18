---
Title: "Signals and Systems Fourier Transform"
Status: 
marker: 
tags: 
Date: "2025.02.13"
Time: "09:56"
---
# Signals and Systems Fourier Transform

## Motivation and Foundation

From previous sections, we understand that analyzing signals and LTI (Linear Time-Invariant) systems requires:
- A set of basic signals that can represent a broad and useful class of signals through linear combinations
- System responses to these basic signals that are simple enough to provide convenient representations for arbitrary input signals

The Fourier Transform emerges as a powerful tool satisfying both requirements by representing signals as combinations of complex exponentials.

## Complex Exponentials as Eigenfunctions

A key insight is that **complex exponentials are eigenfunctions of LTI systems**. For an LTI system with impulse response $h(t)$:

If input: $x(t) = e^{st}$ where $s = \sigma + j\omega$

Then output: $y(t) = H(s)e^{st}$

where $H(s)$ is the eigenvalue (a complex constant that depends only on $s$, not on $t$).

This means the complex exponential passes through the system unchanged in form—only scaled by $H(s)$. This property makes complex exponentials ideal building blocks for signal representation.

## The Fourier Transform Pair

### Analysis Equation (Forward Transform)
The Fourier Transform decomposes a signal $x(t)$ into its frequency components:

$$X(j\omega) = \int_{-\infty}^{\infty} x(t)e^{-j\omega t} \, dt$$

- $X(j\omega)$ is called the **Fourier Transform** or **spectrum** of $x(t)$
- It represents the frequency-domain representation of the signal
- $\omega$ is the angular frequency in radians per second

### Synthesis Equation (Inverse Transform)
The original signal can be reconstructed from its spectrum:

$$x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(j\omega)e^{j\omega t} \, d\omega$$

This shows that any signal $x(t)$ can be expressed as a continuous sum (integral) of complex exponentials $e^{j\omega t}$ with weights $X(j\omega)/2\pi$.

## Physical Interpretation

### Magnitude and Phase Spectrum
The Fourier Transform $X(j\omega)$ is generally complex, so it can be expressed as:

$$X(j\omega) = |X(j\omega)|e^{j\phi(\omega)}$$

where:
- $|X(j\omega)|$ is the magnitude spectrum (amplitude of each frequency component)
- $\phi(\omega)$ is the phase spectrum (phase shift of each frequency component)

### Frequency Domain Perspective
- The Fourier Transform converts time-domain signals into frequency-domain representations
- It reveals which frequencies are present in the signal and their relative strengths
- Low frequencies correspond to slow variations, high frequencies to rapid changes

## System Analysis Using Fourier Transform

For an LTI system with impulse response $h(t)$:

**Frequency Response:**
$$H(j\omega) = \int_{-\infty}^{\infty} h(t)e^{-j\omega t} \, dt$$

The output $Y(j\omega)$ for input $X(j\omega)$ is simply:

$$Y(j\omega) = H(j\omega)X(j\omega)$$

This convolution in time domain becomes multiplication in frequency domain—a major computational advantage.

## Existence Conditions (Dirichlet Conditions)

For $x(t)$ to have a Fourier Transform:

1. $x(t)$ must be absolutely integrable: $\int_{-\infty}^{\infty} |x(t)| \, dt < \infty$
2. $x(t)$ must have finite number of maxima and minima in any finite interval
3. $x(t)$ must have finite number of discontinuities in any finite interval

Note: Some important signals (like constants, unit step, periodic signals) don't satisfy these conditions strictly but can still be handled using generalized Fourier Transforms involving impulses.

## Key Properties

### Linearity
If $x(t) \leftrightarrow X(j\omega)$ and $y(t) \leftrightarrow Y(j\omega)$, then:

$$ax(t) + by(t) \leftrightarrow aX(j\omega) + bY(j\omega)$$

### Time Shifting

$$x(t - t_0) \leftrightarrow e^{-j\omega t_0}X(j\omega)$$

### Frequency Shifting (Modulation)

$$e^{j\omega_0 t}x(t) \leftrightarrow X(j(\omega - \omega_0))$$

### Time Scaling

$$x(at) \leftrightarrow \frac{1}{|a|}X\left(j\frac{\omega}{a}\right)$$

### Duality
If $x(t) \leftrightarrow X(j\omega)$, then:

$$X(jt) \leftrightarrow 2\pi x(-\omega)$$

### Convolution

$$x(t) * y(t) \leftrightarrow X(j\omega)Y(j\omega)$$

(Time-domain convolution = Frequency-domain multiplication)

### Differentiation

$$\frac{dx(t)}{dt} \leftrightarrow j\omega X(j\omega)$$

### Integration

$$\int_{-\infty}^{t} x(\tau) \, d\tau \leftrightarrow \frac{1}{j\omega}X(j\omega) + \pi X(0)\delta(\omega)$$

## Common Transform Pairs

- $\delta(t) \leftrightarrow 1$ (impulse has all frequencies equally)
- $1 \leftrightarrow 2\pi\delta(\omega)$ (DC signal has only zero frequency)
- $e^{-at}u(t) \leftrightarrow \frac{1}{a + j\omega}$ for $a > 0$
- $\text{rect}\left(\frac{t}{T}\right) \leftrightarrow T \cdot \text{sinc}\left(\frac{\omega T}{2}\right)$ (rectangular pulse → sinc function)
- $\text{sinc}(t) \leftrightarrow \pi \cdot \text{rect}\left(\frac{\omega}{2}\right)$ (duality of above)

## Relationship to Other Transforms

- **Fourier Series**: Special case for periodic signals (discrete spectrum)
- **Laplace Transform**: Generalization with $s = \sigma + j\omega$ (Fourier is Laplace with $\sigma = 0$)
- **Discrete-Time Fourier Transform (DTFT)**: For discrete-time signals
- **Discrete Fourier Transform (DFT)**: Discrete time, discrete frequency (computationally implementable)

## Applications

- **Signal Processing**: Filtering, modulation, spectrum analysis
- **Communications**: Frequency multiplexing, bandwidth analysis
- **Control Systems**: Frequency response analysis, stability assessment
- **Image Processing**: 2D Fourier Transform for spatial frequency analysis
- **Audio Processing**: Spectral analysis, equalization, compression

# References


###### Information
- date: 2025.02.13
- time: 09:56