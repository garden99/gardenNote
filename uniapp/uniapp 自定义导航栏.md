# uniapp 自定义导航栏

## 注意事项

ttf字体图标文件不支持彩色，

当navigationStyle设为custom或titleNView设为false时，原生导航栏不显示。这时在进行自定义导航栏组件设置

h5可以使用titleNView创建导航栏（不太灵活，只能满足简单的需求）

使用tabBar属性注册了的页面会具备性能优化策略，页面展示完成会保留在内存中，所以切换 tabbar 页面，只会触发每个页面的onShow，不会再触发onLoad。tabbar页面跳转推荐使用uni.switchTab(OBJECT)进行，可以触发被跳转页面的生命周期

自定义导航栏，可以将页面先设置为tabbar，然后在设置navigationStyle设为custom取消显示，达到性能和自定义同时满足
