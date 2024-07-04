<template>
    <main id="upload-view">
        <ResultsModal :image="image" :imageUrl="imageUrl" v-if="showModal" @close="showModal = false" />
        <div class="center-container">
            <div class="white-container">
                <div class="upload-header">
                    <div class="row default-gap">
                        <vue-feather type="upload" class="round-icon" size="16" />
                        <h4>Upload MRI Image </h4>
                    </div>
                    <p>
                        Please upload the MRI image you would like to analyze. The image should be in PNG/JPEG format.
                    </p>
                </div>
                <div class="upload-form">
                    <IconUpload @click="mediaUpload" v-if="imageUrl === null" />
                    <img :src="imageUrl" alt="" v-else class="upload-preview" />
                    <input type="file" style="display:none" id="fileInput" accept="image/*" @change="imageSelected">
                    <p class="caption-text" v-if="image === null" @click="mediaUpload">Click To Upload Image</p>
                    <p class="caption-text error" @click="removeImage" v-else>Remove Image</p>
                </div>

                <div class="upload-button">
                    <button class="btn-grad" :disabled="image === null" @click="uploadImage">Analyze Image</button>
                </div>
            </div>
        </div>

        <div class="progress-container">
        </div>
    </main>
</template>

<script>
import VueFeather from 'vue-feather';
import IconUpload from '@/components/icons/IconUpload.vue';
import ResultsModal from '@/components/ResultsModal.vue';
export default {
    data() {
        return {
            image: null,
            imageUrl: null,
            showModal: false
        }
    }
    ,
    components: {
        VueFeather, IconUpload, ResultsModal
    },

    methods: {
        mediaUpload() {
            // Upload media from computer
            document.getElementById('fileInput').click();
        },
        imageSelected(e) {
            this.image = e.target.files[0];
            this.imageUrl = URL.createObjectURL(this.image)
        },
        uploadImage() {
            this.showModal = true;
        },
        removeImage() {
            this.image = null;
            this.imageUrl = null;
        }
    }
}
</script>