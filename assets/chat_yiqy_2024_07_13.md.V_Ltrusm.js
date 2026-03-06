import { _ as _export_sfc, C as resolveComponent, o as openBlock, c as createElementBlock, j as createBaseVNode, a as createTextVNode, G as createVNode, w as withCtx } from "./chunks/framework.CE4gUCU2.js";
const __pageData = JSON.parse('{"title":"","description":"","frontmatter":{},"headers":[],"relativePath":"chat/yiqy/2024/07/13.md","filePath":"chat/yiqy/2024/07/13.md"}');
const _sfc_main = { name: "chat/yiqy/2024/07/13.md" };
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  const _component_ChatBubble = resolveComponent("ChatBubble");
  return openBlock(), createElementBlock("div", null, [
    _cache[5] || (_cache[5] = createBaseVNode("h2", {
      id: "_18-00",
      tabindex: "-1"
    }, [
      createBaseVNode("span", { class: "hidden-title" }, "18:00"),
      createTextVNode(),
      createBaseVNode("a", { id: "18:00" }),
      createTextVNode(),
      createBaseVNode("a", {
        class: "header-anchor",
        href: "#_18-00",
        "aria-label": 'Permalink to "<span class="hidden-title">18:00</span> <a id="18:00"></a>"'
      }, "​")
    ], -1)),
    createVNode(_component_ChatBubble, { role: "system" }, {
      default: withCtx(() => _cache[0] || (_cache[0] = [
        createTextVNode(" 18:03 ")
      ])),
      _: 1
    }),
    createVNode(_component_ChatBubble, { role: "system" }, {
      default: withCtx(() => _cache[1] || (_cache[1] = [
        createTextVNode(" 对方撤回了一条消息，保持高贵的沉默。 ")
      ])),
      _: 1
    }),
    createVNode(_component_ChatBubble, {
      role: "user",
      avatar: "https://q.qlogo.cn/g?b=qq&nk=3629489239&s=100",
      id: "msg_7391314919858144818"
    }, {
      default: withCtx(() => _cache[2] || (_cache[2] = [
        createTextVNode(" 这给我推的都是些什么玩意 ")
      ])),
      _: 1
    }),
    _cache[6] || (_cache[6] = createBaseVNode("h2", {
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
      default: withCtx(() => _cache[3] || (_cache[3] = [
        createTextVNode(" 23:28 ")
      ])),
      _: 1
    }),
    createVNode(_component_ChatBubble, { role: "system" }, {
      default: withCtx(() => _cache[4] || (_cache[4] = [
        createTextVNode(" 对方撤回了一条消息，用户 撤回了一条消息 ")
      ])),
      _: 1
    })
  ]);
}
const _13 = /* @__PURE__ */ _export_sfc(_sfc_main, [["render", _sfc_render]]);
export {
  __pageData,
  _13 as default
};
