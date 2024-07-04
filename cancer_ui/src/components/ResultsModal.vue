<template>
    <div class="modal-background" @click="close">
        <div class="modal">
            <div class="white-container">
                <div class="upload-loader" v-if="loading">
                    <flower-spinner :animation-duration="2000" :size="50" color="#000000" />
                    <span>Processing Image</span>
                </div>
                <div class="results-container" v-else>

                    <h3>Lung Hubracious Umaningus</h3>
                    <img :src="imageUrl" alt="">
                    <p>Our AI model has detected a case of Lung Hubracious Umaningus in the uploaded MRI image. We
                        recommend that you consult a medical professional for further diagnosis and treatment.</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { FlowerSpinner } from 'epic-spinners'
export default {
    props: ['image', 'imageUrl'],
    components: {
        FlowerSpinner
    },

    data() {
        return {
            loading: false
        }

    },

    methods: {
        uploadImage() {

        },
        close() {
            this.$emit('close')
        }
    }
}
</script>