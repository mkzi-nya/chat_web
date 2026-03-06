import { _ as _export_sfc, C as resolveComponent, o as openBlock, c as createElementBlock, j as createBaseVNode, a as createTextVNode, G as createVNode, w as withCtx } from "./chunks/framework.CE4gUCU2.js";
const __pageData = JSON.parse('{"title":"","description":"","frontmatter":{},"headers":[],"relativePath":"chat/mhtlim/2024/10/22.md","filePath":"chat/mhtlim/2024/10/22.md"}');
const _sfc_main = { name: "chat/mhtlim/2024/10/22.md" };
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  const _component_ChatBubble = resolveComponent("ChatBubble");
  return openBlock(), createElementBlock("div", null, [
    _cache[5] || (_cache[5] = createBaseVNode("h2", {
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
        createTextVNode(" 阳光下可读性提升 戳了戳 Xeator\\-943 ")
      ])),
      _: 1
    }),
    createVNode(_component_ChatBubble, {
      role: "me",
      avatar: "https://q.qlogo.cn/g?b=qq&nk=2450382239&s=100",
      id: "msg_7428261886341340564"
    }, {
      default: withCtx(() => _cache[2] || (_cache[2] = [
        createTextVNode(" 戳～ ")
      ])),
      _: 1
    }),
    createVNode(_component_ChatBubble, { role: "system" }, {
      default: withCtx(() => _cache[3] || (_cache[3] = [
        createTextVNode(" Chifuyu 戳了戳 阳光下可读性提升 ")
      ])),
      _: 1
    }),
    createVNode(_component_ChatBubble, { role: "system" }, {
      default: withCtx(() => _cache[4] || (_cache[4] = [
        createTextVNode(" Xeator\\-943 戳了戳 阳光下可读性提升 ")
      ])),
      _: 1
    })
  ]);
}
const _22 = /* @__PURE__ */ _export_sfc(_sfc_main, [["render", _sfc_render]]);
export {
  __pageData,
  _22 as default
};
