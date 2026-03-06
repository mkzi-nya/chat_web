import { _ as _export_sfc, C as resolveComponent, o as openBlock, c as createElementBlock, j as createBaseVNode, a as createTextVNode, G as createVNode, w as withCtx } from "./chunks/framework.CE4gUCU2.js";
const __pageData = JSON.parse('{"title":"","description":"","frontmatter":{},"headers":[],"relativePath":"chat/mhtlim/2025/03/21.md","filePath":"chat/mhtlim/2025/03/21.md"}');
const _sfc_main = { name: "chat/mhtlim/2025/03/21.md" };
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  const _component_ChatBubble = resolveComponent("ChatBubble");
  return openBlock(), createElementBlock("div", null, [
    _cache[2] || (_cache[2] = createBaseVNode("h2", {
      id: "_00-00",
      tabindex: "-1"
    }, [
      createBaseVNode("span", { class: "hidden-title" }, "00:00"),
      createTextVNode(),
      createBaseVNode("a", { id: "00:00" }),
      createTextVNode(),
      createBaseVNode("a", {
        class: "header-anchor",
        href: "#_00-00",
        "aria-label": 'Permalink to "<span class="hidden-title">00:00</span> <a id="00:00"></a>"'
      }, "​")
    ], -1)),
    createVNode(_component_ChatBubble, { role: "system" }, {
      default: withCtx(() => _cache[0] || (_cache[0] = [
        createTextVNode(" 00:09 ")
      ])),
      _: 1
    }),
    createVNode(_component_ChatBubble, { role: "system" }, {
      default: withCtx(() => _cache[1] || (_cache[1] = [
        createTextVNode(" 你撤回了一条消息，用户 撤回了一条消息 ")
      ])),
      _: 1
    })
  ]);
}
const _21 = /* @__PURE__ */ _export_sfc(_sfc_main, [["render", _sfc_render]]);
export {
  __pageData,
  _21 as default
};
