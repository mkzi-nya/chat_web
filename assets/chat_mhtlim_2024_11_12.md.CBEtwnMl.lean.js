import { _ as _export_sfc, C as resolveComponent, o as openBlock, c as createElementBlock, j as createBaseVNode, a as createTextVNode, G as createVNode, w as withCtx } from "./chunks/framework.CE4gUCU2.js";
const __pageData = JSON.parse('{"title":"","description":"","frontmatter":{},"headers":[],"relativePath":"chat/mhtlim/2024/11/12.md","filePath":"chat/mhtlim/2024/11/12.md"}');
const _sfc_main = { name: "chat/mhtlim/2024/11/12.md" };
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  const _component_ChatBubble = resolveComponent("ChatBubble");
  return openBlock(), createElementBlock("div", null, [
    _cache[2] || (_cache[2] = createBaseVNode("h2", {
      id: "_12-00",
      tabindex: "-1"
    }, [
      createBaseVNode("span", { class: "hidden-title" }, "12:00"),
      createTextVNode(),
      createBaseVNode("a", { id: "12:00" }),
      createTextVNode(),
      createBaseVNode("a", {
        class: "header-anchor",
        href: "#_12-00",
        "aria-label": 'Permalink to "<span class="hidden-title">12:00</span> <a id="12:00"></a>"'
      }, "​")
    ], -1)),
    createVNode(_component_ChatBubble, { role: "system" }, {
      default: withCtx(() => _cache[0] || (_cache[0] = [
        createTextVNode(" 12:34 ")
      ])),
      _: 1
    }),
    createVNode(_component_ChatBubble, {
      role: "me",
      avatar: "https://q.qlogo.cn/g?b=qq&nk=2450382239&s=100",
      id: "msg_7436250319361622128"
    }, {
      default: withCtx(() => _cache[1] || (_cache[1] = [
        createTextVNode(" （"),
        createBaseVNode("br", null, null, -1),
        createBaseVNode("img", { src: "https://mkzi-nya.github.io/chat_web/resources/images/558B62AA2B928F147938DDEC99BA8709.jpg" }, null, -1)
      ])),
      _: 1
    })
  ]);
}
const _12 = /* @__PURE__ */ _export_sfc(_sfc_main, [["render", _sfc_render]]);
export {
  __pageData,
  _12 as default
};
