import { _ as _export_sfc, C as resolveComponent, o as openBlock, c as createElementBlock, G as createVNode, w as withCtx, a as createTextVNode, j as createBaseVNode } from "./chunks/framework.CE4gUCU2.js";
const __pageData = JSON.parse('{"title":"","description":"","frontmatter":{},"headers":[],"relativePath":"chat/mhtlim/2024/10/16.md","filePath":"chat/mhtlim/2024/10/16.md"}');
const _sfc_main = { name: "chat/mhtlim/2024/10/16.md" };
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  const _component_ChatBubble = resolveComponent("ChatBubble");
  return openBlock(), createElementBlock("div", null, [
    createVNode(_component_ChatBubble, { role: "system" }, {
      default: withCtx(() => _cache[0] || (_cache[0] = [
        createTextVNode(" 23:50 ")
      ])),
      _: 1
    }),
    createVNode(_component_ChatBubble, {
      role: "me",
      avatar: "https://q.qlogo.cn/g?b=qq&nk=2450382239&s=100",
      id: "msg_7426401521006153877"
    }, {
      default: withCtx(() => _cache[1] || (_cache[1] = [
        createBaseVNode("img", { src: "https://mkzi-nya.github.io/chat_web/resources/images/1508101F475641AB7DE4B51C1DADBDFE.jpg" }, null, -1)
      ])),
      _: 1
    })
  ]);
}
const _16 = /* @__PURE__ */ _export_sfc(_sfc_main, [["render", _sfc_render]]);
export {
  __pageData,
  _16 as default
};
