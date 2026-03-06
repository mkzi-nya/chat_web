<template>
  <div v-if="role === 'system'" class="system-msg">
    <slot />
  </div>

  <div
    v-else
    class="chat-row"
    :class="role"
    :data-timestamp="timestamp"
  >
    <a :id="id" class="msg-anchor"></a>

    <img v-if="avatar" :src="avatar" class="avatar" />

    <div ref="bubbleRef" class="chat-bubble" :class="{ image: hasImage }">
      <slot />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick } from "vue"

const props = defineProps({
  role: { type: String, default: "user" },
  avatar: { type: String, default: "" },
  id: { type: String, default: "" },
  timestamp: { type: [String, Number], default: "" }
})

const hasImage = ref(false)
const bubbleRef = ref(null)

function flashTarget(el) {
  el.classList.add("highlight")
  setTimeout(() => {
    el.classList.remove("highlight")
  }, 2000)
}

function scrollToTarget(targetId, smooth = true) {
  const anchor = document.getElementById(targetId)
  if (!anchor) return false

  const row = anchor.closest(".chat-row") || anchor

  row.scrollIntoView({
    behavior: smooth ? "smooth" : "auto",
    block: "center"
  })

  flashTarget(row)
  return true
}

function jumpToTarget(targetId) {
  if (!targetId) return

  const cleanId = targetId.startsWith("#") ? targetId.slice(1) : targetId
  const base = window.location.href.split("#")[0]

  // 强制更新地址
  window.location.href = `${base}#${cleanId}`

  // 再手动滚动一次，避免仅改地址不滚动
  setTimeout(() => {
    scrollToTarget(cleanId, true)
  }, 30)
}

function handleDocumentClick(e) {
  const box = e.target.closest(".reply-box")
  if (!box) return

  e.preventDefault()
  e.stopPropagation()

  const target = box.getAttribute("data-target")
  if (!target) return

  jumpToTarget(target)
}

onMounted(async () => {
  await nextTick()

  if (bubbleRef.value && bubbleRef.value.querySelector("img")) {
    hasImage.value = true
  }

  document.addEventListener("click", handleDocumentClick, true)

  // 首次进入页面如果本身带 hash，也定位一次
  const hash = decodeURIComponent(window.location.hash || "").replace(/^#/, "")
  if (hash) {
    setTimeout(() => {
      scrollToTarget(hash, false)
    }, 150)
  }
})

onUnmounted(() => {
  document.removeEventListener("click", handleDocumentClick, true)
})
</script>

<style scoped>
.chat-row {
  position: relative;
  display: flex;
  align-items: flex-start;
  margin: 10px 0;
  width: 100%;
}

.chat-row.user {
  flex-direction: row;
}

.chat-row.me {
  flex-direction: row-reverse;
}

.msg-anchor {
  position: absolute;
  top: -72px;
  left: 0;
  width: 0;
  height: 0;
  overflow: hidden;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin: 0 10px;
  object-fit: cover;
}

.chat-bubble {
  max-width: 70%;
  padding: 10px 14px;
  border-radius: 18px;
  line-height: 1.6;
  font-size: 15px;
  word-break: break-word;
  box-shadow: 0 2px 6px rgba(0,0,0,.08);
}

.chat-bubble.image {
  padding: 6px;
  background: none;
  box-shadow: none;
}

.chat-bubble.image img {
  max-width: 260px;
  border-radius: 12px;
  display: block;
}

.chat-row.user .chat-bubble {
  background: #f2f3f5;
  color: #1f1f1f;
}

.chat-row.me .chat-bubble {
  background: #cce6ff;
  color: #111;
}

.system-msg {
  width: 100%;
  text-align: center;
  color: rgba(120,120,120,.85);
  font-size: 14px;
  margin: 12px 0;
  user-select: none;
}

:deep(.reply-box) {
  display: block;
  background: rgba(0,0,0,0.06);
  border-radius: 14px;
  padding: 8px 10px;
  margin-bottom: 6px;
  cursor: pointer;
}

:deep(.reply-box:hover) {
  background: rgba(0,0,0,0.1);
}

:deep(.reply-header) {
  font-size: 12px;
  opacity: .65;
  margin-bottom: 4px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

:deep(.reply-text) {
  font-size: 14px;
  opacity: .85;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.highlight {
  animation: flash 2s ease;
}

@keyframes flash {
  0% { background: rgba(200,200,200,.45); }
  100% { background: transparent; }
}

html.dark .chat-row.user .chat-bubble {
  background: #2b2b2b;
  color: #e0e0e0;
}

html.dark .chat-row.me .chat-bubble {
  background: #3b4d65;
  color: #f5f7fa;
}

html.dark :deep(.reply-box) {
  background: rgba(255,255,255,0.08);
}

html.dark :deep(.reply-box:hover) {
  background: rgba(255,255,255,0.14);
}

html.dark .system-msg {
  color: rgba(200,200,200,.65);
}
</style>