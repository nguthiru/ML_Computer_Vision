<template>
    <header>
        <div class="row logo default-gap">
            <img src="@/assets/images/cancer.png" alt="Onco-Vision Logo" class="logo-image" />
            <div class="logotype">
                <span>OncoVision</span>
                <span>Solutions</span>
            </div>
        </div>
        <nav>
            <div class="nav-link">
                <vue-feather type="home" class="nav-icon" size="16" />
                <span>Home</span>
            </div>
            <div class="nav-link">
                <vue-feather type="activity" class="nav-icon" size="16" />
                <span>Predictive Analysis</span>
            </div>
            <RouterLink :to="{ name: 'image_analysis' }">

                <div class="nav-link">
                    <vue-feather type="image" class="nav-icon" size="16" />
                    <span>Image Analysis</span>
                </div>
            </RouterLink>
        </nav>
    </header>
</template>

<script>
import VueFeather from 'vue-feather';

export default {

    components: {
        VueFeather
    }
}
</script>