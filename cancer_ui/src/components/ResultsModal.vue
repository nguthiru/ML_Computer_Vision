<template>
    <div class="modal-background" @click="close">
        <div class="modal">
            <div class="white-container">
                <div class="upload-loader" v-if="loading">
                    <flower-spinner :animation-duration="2000" :size="50" color="#000000" />
                    <span>Processing Image</span>
                </div>
                <div class="results-container" v-else>

                    <h3>{{ classification }}</h3>
                    <img :src="imageUrl" alt="">

                    <p>{{ classifications[classification]['message'] }}</p>
                    <p><strong>Metastasis:</strong> {{ classifications[classification]['metastasis'] }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { FlowerSpinner } from 'epic-spinners'
export default {
    props: ['image', 'imageUrl'],
    components: {
        FlowerSpinner
    },

    data() {
        return {
            loading: true,
            results: null,
            classification: null,
            classifications: {
                'Irrelevant Image': {
                    "metastasis": "None",
                    "message": "The uploaded image does not contain relevant medical information. Please ensure that the image is clear and focused on the area of interest, such as a tumor or abnormality."

                },
                'Colon Adenocarcinoma': {
                    "metastasis": "Liver, Lungs",
                    "message": " Originating from the glandular cells lining the colon. These cells are responsible for producing mucus and other fluids. It typically begins as a benign adenomatous polyp, which can transform into cancer over time if not removed. ",

                },
                "Colon Benign Tissue": {
                    "metastasis": "None",
                    "message": "Non-cancerous cells and structures within the colon. Benign conditions in the colon can include polyps (non-cancerous growths), inflammation, and other non-malignant abnormalities."
                },
                "Lung Adenocarcinoma": {
                    "metastasis": "Brain, Bones, Liver",
                    "message": "A type of non-small cell lung cancer that originates in the glandular cells of the lung. It is the most common type of lung cancer and is often associated with a history of smoking. Adenocarcinoma can spread to other parts of the body, including the brain, bones, and liver."

                },
                "Lung Benign Tissue": {
                    "metastasis": "None",
                    "message": "Non-cancerous cells and structures within the lung. Benign conditions in the lung can include infections, inflammation, and other non-malignant abnormalities."
                },
                "Lung Squamous Cell Carcinoma": {
                    "metastasis": "Lymph Nodes, Liver, Bones",
                    "message": "Lung squamous cell carcinoma (SCC) is a type of non-small cell lung cancer (NSCLC) that arises from the squamous cells lining the airways of the lungs. These cells are flat and cover the surfaces of the airways, protecting them and playing a role in the respiratory system. Lung SCC is closely associated with smoking and tends to develop in the central parts of the lungs, near the main airways (bronchi)."
                }


            }
        }

    },

    methods: {

        uploadImage() {
            var data = new FormData();
            data.append('image', this.image);
            axios.post(
                "http://127.0.0.1:5000/predict",
                data
            )
                .then(response => {
                    this.classification = response.data['predicted_class']
                    this.loading = false;
                })

        },
        close() {
            this.$emit('close')
        }
    },
    mounted() {
        this.uploadImage()
    }
}
</script>