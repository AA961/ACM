<template>
    <header class="bg-bg">
        <div class="container">
            <nav class="jus-between flex align-center ">
                <div class="flex jus-center">
                    <div class="logo">
                        <h3>Ahtisham COD Mobile</h3>
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
        </div>
    </header>
</template>

<style lang="scss" scoped>
header {
    padding: 2rem 0rem;

    h3 {
        color: var(--text);
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
</style>