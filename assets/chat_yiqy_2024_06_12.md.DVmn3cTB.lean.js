import { _ as _export_sfc, C as resolveComponent, o as openBlock, c as createElementBlock, j as createBaseVNode, a as createTextVNode, G as createVNode, w as withCtx } from "./chunks/framework.CE4gUCU2.js";
const __pageData = JSON.parse('{"title":"","description":"","frontmatter":{},"headers":[],"relativePath":"chat/yiqy/2024/06/12.md","filePath":"chat/yiqy/2024/06/12.md"}');
const _sfc_main = { name: "chat/yiqy/2024/06/12.md" };
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  const _component_ChatBubble = resolveComponent("ChatBubble");
  return openBlock(), createElementBlock("div", null, [
    _cache[2] || (_cache[2] = createBaseVNode("h2", {
      id: "_01-00",
      tabindex: "-1"
    }, [
      createBaseVNode("span", { class: "hidden-title" }, "01:00"),
      createTextVNode(),
      createBaseVNode("a", { id: "01:00" }),
      createTextVNode(),
      createBaseVNode("a", {
        class: "header-anchor",
        href: "#_01-00",
        "aria-label": 'Permalink to "<span class="hidden-title">01:00</span> <a id="01:00"></a>"'
      }, "​")
    ], -1)),
    createVNode(_component_ChatBubble, { role: "system" }, {
      default: withCtx(() => _cache[0] || (_cache[0] = [
        createTextVNode(" 01:39 ")
      ])),
      _: 1
    }),
    createVNode(_component_ChatBubble, { role: "system" }, {
      default: withCtx(() => _cache[1] || (_cache[1] = [
        createTextVNode(" 对方撤回了一条消息，因为有错别字。 ")
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
