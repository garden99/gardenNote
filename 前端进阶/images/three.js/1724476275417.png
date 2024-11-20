<template>
  <view class="content">
    <view id="threeView"></view>

    <image class="logo" src="/static/logo.png"></image>
    <view class="text-area">
      <text class="title">{{ title }}</text>
      <view id="three" class="three" @click="three.onClick"></view>
      <!-- <canvas
        style="width: 3000px; height: 2000px"
        canvas-id="firstCanvas"
        id="firstCanvas"
      ></canvas> -->
    </view>
  </view>
</template>

<script>
// import * as THREE from "three";
const THREE = require('three/build/three.cjs')

// import {OrbitControls} from 'three/examples/jsm/controls/OrbitControls.js'

import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
import { OBJLoader } from "three/examples/jsm/loaders/OBJLoader.js";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";

// const three = require('three')
export default {
  data() {
    return {
      title: "Hello",
      scene: null,
      camera: null,
      renderer: null,
    };
  },
  mounted() {
    console.log(THREE);
    console.log(OrbitControls);
    console.log(GLTFLoader);
    console.log(document);
    console.log(window);

    this.threed();
  },
  methods: {
    threed() {
      const that = this;
        const canvas = document.createElement("canvas");
        canvas.width = 1000; // 设置画布宽度为浏览器窗口宽度
        canvas.height = 1000; // 设置画布高度为浏览器窗口高度
        canvas.width = window.innerWidth; // 设置画布宽度为浏览器窗口宽度
        canvas.height = window.innerHeight; // 设置画布高度为浏览器窗口高度
        document.body.appendChild(canvas);

      // 渲染器
       const renderer = new THREE.WebGLRenderer({ canvas });

      // const element = document.getElementById("threeView");
      // console.log(element);

      // let renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
      // renderer.physicallyCorrectLights = true;
      // renderer.outputEncoding = THREE.sRGBEncoding;
      // renderer.setPixelRatio(window.devicePixelRatio);
      // renderer.setSize(window.innerWidth, window.innerHeight);
      // let pmremGenerator = new THREE.PMREMGenerator(renderer);
      // pmremGenerator.compileEquirectangularShader();
      // element.appendChild(renderer.domElement); // body元素中插入canvas对象F

      const fov = 400; // 视野范围
      const aspect = window.innerWidth / window.innerHeight; // 画布的宽高比
      const near = 0.1; // 近平面
      const far = 1000; // 远平面
      // 透视投影相机
      that.camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
      that.camera.position.set(0, 0, 20);
      that.camera.lookAt(0, 0, 0);
      // 控制相机
      const controls = new OrbitControls(that.camera, renderer.domElement);

      // 场景
      that.scene = new THREE.Scene();
      that.scene.background = new THREE.Color("green");

      {
        // 半球光
        const skyColor = 0xb1e1ff; // 蓝色
        const groundColor = 0xffffff; // 白色
        const intensity = 1;
        const light = new THREE.HemisphereLight(
          skyColor,
          groundColor,
          intensity
        );
        that.scene.add(light);
      }

      {
        // 方向光
        const color = 0xffffff;
        const intensity = 1;
        const light = new THREE.DirectionalLight(color, intensity);
        light.position.set(0, 10, 0);
        light.target.position.set(-5, 0, 0);
        that.scene.add(light);
        that.scene.add(light.target);
      }

      // 渲染循环
      const animate = () => {
        requestAnimationFrame(animate);
        // that.controls.update();
        renderer.render(that.scene, that.camera);
      };
      {
        const objLoader = new OBJLoader();
        // const gLTFLoader = new GLTFLoader();
        const color = "#bb1965";
        // setTimeout(() => {
        //     color = "green"
        // }, 1000);
        objLoader.load("/static/mao.obj", (object) => {
          object.position.set(0, -4, 0); // 调整模型位置
          object.scale.set(1, 1, 1);
          that.scene.add(object);
          animate();
          //   requestAnimationFrame(that.render);
        });
      }
    },
    // render() {
    //   this.renderer.render(this.scene, this.camera);
    //   requestAnimationFrame(this.render);
    // },
  },
};
</script>

<style>
.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.logo {
  height: 200rpx;
  width: 200rpx;
  margin-top: 200rpx;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 50rpx;
}

.text-area {
  display: flex;
  justify-content: center;
}

.title {
  font-size: 36rpx;
  color: #8f8f94;
}
</style>
