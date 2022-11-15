<template>
    <header class="bg-bg">
        <div class="container">
            <nav class="jus-between flex align-center ">
                <div class="flex jus-center">
                    <div class="logo">
                        <h3>ACM</h3>
                    </div>
                </div>

                <div class="nav-links flex align-center jus-between">
                    <a href="#">Home</a>
                    <a href="#">Videos</a>
                    <a href="#">About</a>
                    <a href="#">Partner</a>
                </div>

                <div class="nav-search">
                    <i class="fa fa-search"></i>
                </div>

            </nav>

            <div class="hero flex jus-between align-center">

                <div class="left">
                    <h4>--Welcome to</h4>
                    <h2>Ahtisham</h2>
                    <h1 class="heading">COD Mobile</h1>
                    <p>Bringing you the best gameplay <br> and latest leaks of the Call of Duty.</p>
                    <a href="https://www.youtube.com/c/AhtishamCODMobile" target="_blank">
                        <button class="btn-secondry btn m1-top">Subscribe</button>
                    </a>
                </div>

                <div class="right">
                    <img src="../assets/imgs/cod.png" alt="">
                </div>

            </div>
        </div>
    </header>
</template>

<script setup>

</script>

<style lang="scss" scoped>
header {
    padding: 2rem 0rem;

    h3 {
        color: var(--text);
        font-size: 24px;
    }

    nav {
        @media (max-width:1000px) {
            display: none;
        }

        .nav-links {
            a {
                color: var(--text);
                margin: 0rem 3rem;
                text-decoration: none;
                font-weight: 600;
                display: inline-block;
                position: relative;

                &::after {
                    content: '';
                    position: absolute;
                    width: 100%;
                    transform: scaleX(0);
                    height: 2px;
                    bottom: 0;
                    left: 0;
                    background-color: var(--text);
                    transform-origin: bottom right;
                    transition: transform 0.25s ease-out;
                }

                &:hover::after {
                    transform: scaleX(1);
                    transform-origin: bottom left;
                }
            }
        }

        .nav-search {
            i {
                font-size: 24px;
                cursor: pointer;
                color: var(--text);
                font-weight: 600;
            }
        }
    }



    .hero {
        // padding: 0 3rem;
        padding-top: 1rem;
        padding-bottom: -1rem;

        @media (max-width:950px) {
            flex-direction: column;
            padding: 6rem 0;
            justify-content: center;
            align-items: center;
            text-align: center;
        }

        .left {
            flex: 1;

            @media (max-width:576px) {
                text-align: center;
            }

            h4 {
                font-size: 1rem;
                color: var(--text);
                letter-spacing: 4px;
            }

            h2 {
                font-size: 3rem;
                letter-spacing: 4px;
                color: var(--text);
            }

            h1 {
                font-size: 4.2rem;
                color: #fffac3;
                margin-top: -1rem;
                letter-spacing: 4px;

                @media (max-width:576px) {
                    line-height: 4rem;
                    margin-top: 0;
                    margin-bottom: 1rem;
                }
            }

            p {
                font-size: 1.2rem;
                color: var(--text);
                letter-spacing: 4px;
                line-height: 2rem;
            }

            button {
                margin-top: 2rem;
            }
        }

        .right {


            @media (max-width:950px) {
                display: none;
                flex: 0;
            }

            flex: 1;
            // overflow: hidden;
            margin: 8px;
            // min-width: 240px;
            // max-width: 400px;
            width: 100%;
            transform: translateY(47px);

            // &:hover {
            //     img {
            //         transform: scale(1.3) rotate(5deg);
            //     }
            // }

            img {
                transition: all 0.3s;
                box-sizing: border-box;
                max-width: 600px;
                height: 600px;
                // text-shadow: 0px -10px 30px #ccc;
            }
        }

    }
}
</style>