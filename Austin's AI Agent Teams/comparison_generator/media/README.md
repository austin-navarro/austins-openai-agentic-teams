# Media Directory

This directory stores generated comparison images created by the Image Generator Agent.

## Image Specifications
- Format: JPG/PNG
- Dimensions: 1200x675px (16:9 aspect ratio)
- Naming Convention: `{mediaId}.{extension}`
  - Example: `bitcoin-vs-ethereum.jpg`

## Usage
- Images are generated using DALL-E 2
- Each image corresponds to a comparison JSON file in the `outputs/` directory
- The `mediaId` is used to link images with their respective comparison content

## Notes
- Images should be visually appealing and clearly represent both comparison subjects
- Horizontal format is preferred for better blog presentation
- File names must match the `mediaId` used in the comparison JSON files 