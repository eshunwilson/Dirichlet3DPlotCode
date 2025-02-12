# Dirichlet3DPlotCode
 🎲 3D Visualization of Dirichlet Distribution Samples

This repository contains a Python script that generates random samples from a Dirichlet distribution and visualizes them in 3D space. The Dirichlet distribution is widely used in probabilistic modeling, Bayesian statistics, and machine learning, especially for modeling categorical probabilities.

📊 Features

✅ Generate Random Samples – Draws samples from a Dirichlet distribution using customizable parameters.

✅ 3D Scatter Plot – Visualizes the samples in 3D space to show their distribution across probability simplex.

✅ Colormap Intensity – Uses color mapping to represent variations in the Z component.

✅ Adjustable Parameters – Modify the alpha values to explore different Dirichlet behaviors.

📌 How It Works

1️⃣ Set Dirichlet parameters (alpha values) to control distribution shape.

2️⃣ Generate random samples using NumPy’s np.random.dirichlet().

3️⃣ Extract components (X, Y, Z) from the samples.

4️⃣ Plot the samples in a 3D space using Matplotlib’s Axes3D.

5️⃣ Apply colormap intensity based on the Z component.

Example Output

The script will generate a 3D scatter plot where each point represents a randomly sampled probability vector from the Dirichlet distribution.

🔬 Scientific Relevance

✔ Bayesian Statistics – Dirichlet distribution is commonly used as a prior in categorical models.

✔ Machine Learning – Core component of Latent Dirichlet Allocation (LDA) for topic modeling.

✔ Probability & Simplex Constraints – Used in genetics, ecology, and finance for modeling proportions.

🛠 Future Improvements

🔹 Add interactive plotting using plotly for better exploration.

🔹 Implement different Dirichlet parameter sets for comparative visualization.

🔹 Extend visualization to higher dimensions (e.g., Dirichlet in 4D?).

📜 License

This project is open-source under the MIT License. Feel free to use and modify!
