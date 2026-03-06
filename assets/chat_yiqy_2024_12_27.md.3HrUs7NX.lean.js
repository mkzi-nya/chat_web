import { _ as _export_sfc, C as resolveComponent, o as openBlock, c as createElementBlock, j as createBaseVNode, a as createTextVNode, G as createVNode, w as withCtx } from "./chunks/framework.CE4gUCU2.js";
const __pageData = JSON.parse('{"title":"","description":"","frontmatter":{},"headers":[],"relativePath":"chat/yiqy/2024/12/27.md","filePath":"chat/yiqy/2024/12/27.md"}');
const _sfc_main = { name: "chat/yiqy/2024/12/27.md" };
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  const _component_ChatBubble = resolveComponent("ChatBubble");
  return openBlock(), createElementBlock("div", null, [
    _cache[2] || (_cache[2] = createBaseVNode("h2", {
      id: "_07-00",
      tabindex: "-1"
    }, [
      createBaseVNode("span", { class: "hidden-title" }, "07:00"),
      createTextVNode(),
      createBaseVNode("a", { id: "07:00" }),
      createTextVNode(),
      createBaseVNode("a", {
        class: "header-anchor",
        href: "#_07-00",
        "aria-label": 'Permalink to "<span class="hidden-title">07:00</span> <a id="07:00"></a>"'
      }, "​")
    ], -1)),
    createVNode(_component_ChatBubble, { role: "system" }, {
      default: withCtx(() => _cache[0] || (_cache[0] = [
        createTextVNode(" 07:18 ")
      ])),
      _: 1
    }),
    createVNode(_component_ChatBubble, {
      role: "user",
      avatar: "https://q.qlogo.cn/g?b=qq&nk=2416523958&s=100",
      id: "msg_7452957454208875447"
    }, {
      default: withCtx(() => _cache[1] || (_cache[1] = [
        createTextVNode(" 早 ")
      ])),
      _: 1
    })
  ]);
}
const _27 = /* @__PURE__ */ _export_sfc(_sfc_main, [["render", _sfc_render]]);
export {
  __pageData,
  _27 as default
};
