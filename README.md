# Distance Classification

This repository contains the code and resources for the Machine Learning Pattern Recognition (MLPR) Lab project on distance-based classification methods. The project focuses on implementing and comparing various distance metrics for classifying data points, with practical applications in image clustering and face recognition.

## Project Overview

Distance-based classification is a fundamental approach in machine learning, where the similarity between data points is quantified using distance metrics. This project explores different distance measures and their effectiveness in classification tasks. Key components of the project include:

- **Implementation of Distance Metrics**: The project implements various distance metrics such as Euclidean, Manhattan, and Mahalanobis distances. These metrics are essential for algorithms like k-Nearest Neighbors (k-NN) and clustering methods. citeturn0search1

- **Face Detection and Clustering**: Utilizing the implemented distance metrics, the project performs face detection and clustering on a set of images. This involves detecting faces within images and grouping similar faces together based on the chosen distance measures.

![clustered_faces](https://github.com/user-attachments/assets/a2360023-7867-496b-8a7e-1ceb7bd7b4fe)
![Clustering with template image](https://github.com/user-attachments/assets/4044afd5-ccd8-4551-83f1-24690abe4fb5)
![detected faces](https://github.com/user-attachments/assets/e934530d-6b97-4dd1-8067-750c2e5961d3)
![Scatter plot clustering with template image](https://github.com/user-attachments/assets/24bc4ce8-86d3-4f8b-972c-df5e594b7065)
![scatter plot face clustering](https://github.com/user-attachments/assets/186e808c-365e-4971-afa5-5d54d6a86868)


## Repository Structure

The repository is organized as follows:

- `AryanDaga_Lab5.ipynb`: Jupyter Notebook containing the main code and analysis for the project.
- `distance_classification.py`: Python script implementing the distance-based classification functions.
- `verify_files.py`: Script to verify the presence and integrity of required files.
- `Dockerfile`: Configuration file for creating a Docker container to run the project in a consistent environment.
- `images/`: Directory containing images used in the project, including:
  - `Dr_Shashi_Tharoor.jpg`: Sample image for face detection.
  - `Plaksha_Faculty.jpg`: Image containing multiple faces for clustering.
  - `clustered_faces.png`: Output image showing clustered faces.
  - `detected_faces.jpg`: Image highlighting detected faces.
  - `scatter_plot_clustering.png`: Scatter plot visualizing clustering results.

## Getting Started

To run the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/aryandaga/distance_classification.git
   cd distance_classification
   ```

2. **Set Up the Environment**:
   - **Using Docker**:
     - Build the Docker image:
       ```bash
       docker build -t distance_classification .
       ```
     - Run the Docker container:
       ```bash
       docker run -it --rm -v $(pwd):/app distance_classification
       ```
   - **Without Docker**:
     - Ensure you have Python 3.x installed.
     - Install the required packages:
       ```bash
       pip install -r requirements.txt
       ```

3. **Run the Jupyter Notebook**:
   ```bash
   jupyter notebook AryanDaga_Lab5.ipynb
   ```
   This will open the notebook in your default web browser, allowing you to execute the code cells and explore the analysis.

## Results

The project demonstrates the application of distance-based classification in clustering faces from images. By experimenting with different distance metrics, the project provides insights into how each metric affects the clustering outcomes. Visualizations such as scatter plots and clustered face images are included to illustrate the results.

## References

- [Distance Metrics in Machine Learning](https://www.analyticsvidhya.com/blog/2020/02/4-types-of-distance-metrics-in-machine-learning/)
- [Distance-Based Classification Example](https://github.com/Anagha-Sankar/Distance-Based-Classification)

For more information on distance metrics and their applications, refer to the provided links.

---

*Note: This project is part of the MLPR Lab coursework and is intended for educational purposes.* 

