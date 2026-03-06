import { _ as _export_sfc, C as resolveComponent, o as openBlock, c as createElementBlock, j as createBaseVNode, a as createTextVNode, G as createVNode, w as withCtx } from "./chunks/framework.CE4gUCU2.js";
const __pageData = JSON.parse('{"title":"","description":"","frontmatter":{},"headers":[],"relativePath":"chat/yiqy/2025/03/15.md","filePath":"chat/yiqy/2025/03/15.md"}');
const _sfc_main = { name: "chat/yiqy/2025/03/15.md" };
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  const _component_ChatBubble = resolveComponent("ChatBubble");
  return openBlock(), createElementBlock("div", null, [
    _cache[2] || (_cache[2] = createBaseVNode("h2", {
      id: "_10-00",
      tabindex: "-1"
    }, [
      createBaseVNode("span", { class: "hidden-title" }, "10:00"),
      createTextVNode(),
      createBaseVNode("a", { id: "10:00" }),
      createTextVNode(),
      createBaseVNode("a", {
        class: "header-anchor",
        href: "#_10-00",
        "aria-label": 'Permalink to "<span class="hidden-title">10:00</span> <a id="10:00"></a>"'
      }, "​")
    ], -1)),
    createVNode(_component_ChatBubble, { role: "system" }, {
      default: withCtx(() => _cache[0] || (_cache[0] = [
        createTextVNode(" 10:35 ")
      ])),
      _: 1
    }),
    createVNode(_component_ChatBubble, {
      role: "user",
      avatar: "https://q.qlogo.cn/g?b=qq&nk=2416523958&s=100",
      id: "msg_7481919243782222448"
    }, {
      default: withCtx(() => _cache[1] || (_cache[1] = [
        createBaseVNode("img", { src: "https://mkzi-nya.github.io/chat_web/resources/images/A6FCB737F3E6AE8835CACFB5B295E179.jpg" }, null, -1)
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
