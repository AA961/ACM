<template>
    <sliderVue></sliderVue>


    <section id="new-vid">
        <div class="container">
            <div class="left">
                <img src="../assets/imgs/vlogger_v1_home_videos_slide_1.png" alt="">
            </div>
            <div class="right">
                <h4>New Videos!</h4>
                <h2>Every Day at 6PM.</h2>
                <p>

                    Remember to <span> turn on the notifications</span> bell so you’ll be informed when a new video is
                    uploaded! <br> <br> <br>

                    We really appreaciate all your comments, likes and suggestions, so keep em coming!
                </p>

                <button class="btn btn-primary m1-top m1-bottom">Subscribe Now</button>
            </div>
        </div>
    </section>


   
</template>

<script setup>
import sliderVue from './slider.vue';
</script>


<style lang="scss" scoped>
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    flex-direction: column;
}

#new-vid {
    color: var(--dark);
    margin-top: 4rem;

    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;

        .left {
            display: flex;
            justify-content: center;
            align-items: center;

            img {
                width: 80%;
            }
        }

        .right {

            h2 {
                font-size: 3rem;
            }

            p {
                // color: var(--light);
                font-weight: 400;
                font-size: 1.2rem;

                span {
                    color: var(--dark);
                    font-weight: 600;
                }
            }
        }
    }
}
</style>