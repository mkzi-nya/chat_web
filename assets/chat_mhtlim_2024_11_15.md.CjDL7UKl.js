import { _ as _export_sfc, C as resolveComponent, o as openBlock, c as createElementBlock, j as createBaseVNode, a as createTextVNode, G as createVNode, w as withCtx } from "./chunks/framework.CE4gUCU2.js";
const __pageData = JSON.parse('{"title":"","description":"","frontmatter":{},"headers":[],"relativePath":"chat/mhtlim/2024/11/15.md","filePath":"chat/mhtlim/2024/11/15.md"}');
const _sfc_main = { name: "chat/mhtlim/2024/11/15.md" };
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  const _component_ChatBubble = resolveComponent("ChatBubble");
  return openBlock(), createElementBlock("div", null, [
    _cache[7] || (_cache[7] = createBaseVNode("h2", {
      id: "_23-00",
      tabindex: "-1"
    }, [
      createBaseVNode("span", { class: "hidden-title" }, "23:00"),
      createTextVNode(),
      createBaseVNode("a", { id: "23:00" }),
      createTextVNode(),
      createBaseVNode("a", {
        class: "header-anchor",
        href: "#_23-00",
        "aria-label": 'Permalink to "<span class="hidden-title">23:00</span> <a id="23:00"></a>"'
      }, "​")
    ], -1)),
    createVNode(_component_ChatBubble, { role: "system" }, {
      default: withCtx(() => _cache[0] || (_cache[0] = [
        createTextVNode(" 23:05 ")
      ])),
      _: 1
    }),
    createVNode(_component_ChatBubble, {
      role: "me",
      avatar: "https://q.qlogo.cn/g?b=qq&nk=2450382239&s=100",
      id: "msg_7511739357107402012"
    }, {
      default: withCtx(() => _cache[1] || (_cache[1] = [
        createBaseVNode("img", { src: "https://mkzi-nya.github.io/chat_web/resources/images/FE42CA8D721F3919C3492AA91D17C874.jpg" }, null, -1)
      ])),
      _: 1
    }),
    createVNode(_component_ChatBubble, { role: "system" }, {
      default: withCtx(() => _cache[2] || (_cache[2] = [
        createTextVNode(" 23:18 ")
      ])),
      _: 1
    }),
    createVNode(_component_ChatBubble, { role: "system" }, {
      default: withCtx(() => _cache[3] || (_cache[3] = [
        createTextVNode(" libchara\\-devv 回应了你的 消息: ")
      ])),
      _: 1
    }),
    createVNode(_component_ChatBubble, {
      role: "user",
      avatar: "https://q.qlogo.cn/g?b=qq&nk=2624521592&s=100",
      id: "msg_7437673731833285868"
    }, {
      default: withCtx(() => _cache[4] || (_cache[4] = [
        createBaseVNode("div", {
          class: "reply-box",
          "data-target": "msg_7511739357107402012"
        }, [
          createBaseVNode("div", { class: "reply-header" }, "归梦 23:05"),
          createBaseVNode("div", { class: "reply-text" }, "\\[图片\\]")
        ], -1),
        createBaseVNode("br", null, null, -1),
        createTextVNode("有没有可能你是群主 ")
      ])),
      _: 1
    }),
    createVNode(_component_ChatBubble, {
      role: "me",
      avatar: "https://q.qlogo.cn/g?b=qq&nk=2450382239&s=100",
      id: "msg_7437673731833285858"
    }, {
      default: withCtx(() => _cache[5] || (_cache[5] = [
        createTextVNode(" 我不管，反正冒个泡 ")
      ])),
      _: 1
    }),
    createVNode(_component_ChatBubble, {
      role: "me",
      avatar: "https://q.qlogo.cn/g?b=qq&nk=2450382239&s=100",
      id: "msg_7437673731833285852"
    }, {
      default: withCtx(() => _cache[6] || (_cache[6] = [
        createBaseVNode("img", { src: "https://mkzi-nya.github.io/chat_web/resources/images/FBC437306EFCB8883427BDB9304C7E59.jpg" }, null, -1)
      ])),
      _: 1
    })
  ]);
}
const _15 = /* @__PURE__ */ _export_sfc(_sfc_main, [["render", _sfc_render]]);
export {
  __pageData,
  _15 as default
};
