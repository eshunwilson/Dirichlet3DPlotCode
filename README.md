# Dirichlet3DPlotCode
 3D Visualization of Dirichlet Distribution Samples

This repository contains a Python script that generates random samples from a Dirichlet distribution and visualizes them in 3D space. The Dirichlet distribution is widely used in probabilistic modeling, Bayesian statistics, and machine learning, especially for modeling categorical probabilities.

Features

Generate Random Samples – Draws samples from a Dirichlet distribution using customizable parameters.

3D Scatter Plot – Visualizes the samples in 3D space to show their distribution across probability simplex.

Colormap Intensity – Uses color mapping to represent variations in the Z component.

Adjustable Parameters – Modify the alpha values to explore different Dirichlet behaviors.

How It Works

Set Dirichlet parameters (alpha values) to control distribution shape.

Generate random samples using NumPy’s np.random.dirichlet().

Extract components (X, Y, Z) from the samples.

Plot the samples in a 3D space using Matplotlib’s Axes3D.

Apply colormap intensity based on the Z component.

Example Output

The script will generate a 3D scatter plot where each point represents a randomly sampled probability vector from the Dirichlet distribution.

Scientific Relevance

✔ Bayesian Statistics – Dirichlet distribution is commonly used as a prior in categorical models.

✔ Machine Learning – Core component of Latent Dirichlet Allocation (LDA) for topic modeling.

✔ Probability & Simplex Constraints – Used in genetics, ecology, and finance for modeling proportions.

