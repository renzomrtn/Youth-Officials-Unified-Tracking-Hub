<template>
    <div class="navbar">
        <p>burger</p>
        <div class="branding">
            <img class="brand-image" src="../assets/youth-ims-logo.svg" />
            <div class="vl"></div>
            <div class="app-name">
                <h3>YOUTH</h3>
                <h6>Youth Officials' Unified Tracking Hub</h6>
            </div>
        </div>
        <p>breadcrumb</p>
        <p>mode</p>
        <p>account</p>
    </div>
</template>

<style scoped>
.navbar {
    background-color: #ffffff;
    display: flex;
    justify-content: space-between;
    padding: 16px;
    border-bottom: #e5e7eb 1px solid;
}

.branding {
    color: 000000;
    display: flex;
    justify-content: center;
    align-items: center;
}

.brand-image {
    width: 3rem;
}

.vl {
  border-left: 6px solid rgb(0, 0, 0);
  height: 100%;
  margin: 0 5px 0 5px;
}
</style>