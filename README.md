# Fuzzy-Based GI Image Classification

A deep learning framework for classifying gastrointestinal (GI) tract images using an ensemble of pre-trained CNNs enhanced with fuzzy logic, MC Dropout, and ResNeXt blocks for improved accuracy and uncertainty estimation.

## Overview

This project implements an advanced ensemble model combining MobileNetV2, ResNet101V2, and Xception architectures with the following enhancements:
- **Fuzzy logic integration** for uncertainty-aware predictions
- **Monte Carlo (MC) Dropout** for prediction reliability
- **ResNeXt blocks** for improved feature extraction
- **Attention mechanisms** for better model interpretability

The model achieves **96.7% accuracy** on a combined dataset of polyps and GI tract abnormalities.

## Dataset

The framework uses a combined dataset from two sources:

### Kvasir Dataset
- **Polyps**: 1,000 images
- **Esophagitis**: 1,000 images  
- **Normal Cecum**: 1,000 images
- **Ulcerative Colitis**: 1,000 images

### ETIS-Larib Polyp Database
- **Polyps**: 392 images

**Total**: 4,392 images
- Training: 3,513 images (80%)
- Testing: 879 images (20%)

## Model Architecture

### Base Models
Three pre-trained models form the ensemble foundation:
1. **MobileNetV2** - Lightweight and efficient
2. **ResNet101V2** - Deep residual learning
3. **Xception** - Depthwise separable convolutions

### Key Components

#### ResNeXt Blocks
- Cardinality = 32
- Group convolutions for parallel feature learning
- Enhanced representational power

#### MC Dropout
- Dropout rate: 0.5
- Multiple stochastic forward passes (20 samples)
- Enables uncertainty quantification

#### Fuzzy Logic Layer
- Triangular membership functions
- Defuzzification using center-of-gravity method
- Weighted uncertainty estimation with optimal p-value = 6

## Performance

### Final Results
- **Overall Accuracy**: 96.7%
- **Best p-value**: 6 (from ensemble ablation study)
- **MC Samples**: 20

### Per-Class Metrics

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| Polyps | 0.97 | 0.93 | 0.95 | 279 |
| Esophagitis | 1.00 | 1.00 | 1.00 | 200 |
| Normal Cecum | 0.91 | 0.98 | 0.94 | 200 |
| Ulcerative Colitis | 0.95 | 0.94 | 0.95 | 200 |

### Training Configuration
- **Epochs**: 50 (with early stopping)
- **Batch size**: 16
- **Image size**: 224×224 pixels
- **Optimizer**: Adam (learning rate: 0.001)
- **Data augmentation**: Random flip, rotation, zoom, brightness, contrast

## Requirements


## Future Work

- Extend to additional GI abnormality classes
- Implement explainability techniques (Grad-CAM, SHAP)
- Deploy as REST API for clinical integration
- Real-time video analysis for endoscopy procedures

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Kvasir dataset providers
- ETIS-Larib Polyp Database contributors
- TensorFlow/Keras team for pre-trained models

## Contact

For questions or collaborations:
- **GitHub**: [@kethanreddy407-create](https://github.com/kethanreddy407-create)
- **Repository**: [Fuzzy_Based_GI_Image_Classification](https://github.com/kethanreddy407-create/Fuzzy_Based_GI_Image_Classification)
