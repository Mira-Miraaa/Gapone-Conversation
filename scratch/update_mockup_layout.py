import re

file_path = r"c:\Users\ManhTV\Documents\Antigravity\Gapone-Conversation\Mockup\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Left menu changes: Put Contact between Dashboard and Conversations
# Let's find the menu block and move it.
menu_item_dashboard = """                    <div class="menu-item" onclick="selectMenu(this)">
                        <div class="menu-item-link">
                            <span class="menu-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="9" rx="1"></rect><rect x="14" y="3" width="7" height="5" rx="1"></rect><rect x="14" y="12" width="7" height="9" rx="1"></rect><rect x="3" y="16" width="7" height="5" rx="1"></rect></svg>
                            </span>
                            <span class="menu-text">Bảng điều khiển</span>
                        </div>
                    </div>"""

menu_item_conversation = """                    <div class="menu-item" onclick="selectMenu(this)">
                        <div class="menu-item-link">
                            <span class="menu-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
                            </span>
                            <span class="menu-text">Hội thoại</span>
                        </div>
                    </div>"""

menu_item_contacts = """                    <div class="menu-item" id="menu-item-contacts" onclick="navigateSubmenu('contacts')">
                        <div class="menu-item-link">
                            <span class="menu-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                            </span>
                            <span class="menu-text">Liên hệ</span>
                        </div>
                    </div>"""

# Remove old placements and place in order: Dashboard -> Contacts -> Conversation
html = html.replace(menu_item_dashboard, "")
html = html.replace(menu_item_conversation, "")
html = html.replace(menu_item_contacts, "")

menu_start_tag = '<nav class="sidebar-menu">'
replacement_menu = menu_start_tag + "\n" + menu_item_dashboard + "\n\n" + menu_item_contacts + "\n\n" + menu_item_conversation
html = html.replace(menu_start_tag, replacement_menu)


# 2. Remove requested text strings:
# - "Quản lý và đồng bộ thông tin liên hệ khách hàng giữa GapOne và GapOne Conversation (Shared Contact DB)"
html = html.replace(
    '<p class="settings-subtitle">Quản lý và đồng bộ thông tin liên hệ khách hàng giữa GapOne và GapOne Conversation (Shared Contact DB)</p>',
    ''
)
# - "Tạo mới thông tin liên hệ khách hàng vào hệ thống"
html = html.replace(
    '<p class="settings-subtitle" id="contact-form-subtitle">Tạo mới thông tin liên hệ khách hàng vào hệ thống</p>',
    '<p class="settings-subtitle" id="contact-form-subtitle"></p>'
)
# - "Cập nhật thông tin khách hàng"
# Wait! In javascript we set title and subtitle dynamically. Let's make sure it is cleared there too!
# Let's inspect where "Cập nhật thông tin khách hàng" is. It was inside the openContactFormPage function:
# subtitleEl.innerText = "Cập nhật thông tin khách hàng";
html = html.replace(
    'subtitleEl.innerText = "Cập nhật thông tin khách hàng";',
    'subtitleEl.innerText = "";'
)


# 3. Align settings-card in contact form view and remove max-width: 800px to fix white space gap on right.
html = html.replace(
    '<div class="settings-card" style="max-width: 800px; padding: 24px;">',
    '<div class="settings-card" style="padding: 24px;">'
)


# 4. Modify Avatar upload field layout (Item 5):
# Place the text placeholder inside the text input box, put an upload button next to it.
old_avatar_field = """                            <div class="form-group">
                                <label class="form-label">Ảnh đại diện</label>
                                <span style="font-size:11px; color:var(--text-muted); display:block; margin-bottom:4px;">Chỉ cho phép các định dạng sau: .jpg, .png, .jpeg</span>
                                <input type="file" id="contact-form-avatar" class="form-control" style="padding: 6px;" accept=".jpg,.jpeg,.png" onchange="validateAvatarUpload(this)">
                                <span id="err-avatar" style="color: #ef4444; font-size: 11px; display: none; margin-top: 4px;">Chỉ cho phép các định dạng sau: .jpg, .png, .jpeg</span>
                            </div>"""

new_avatar_field = """                            <div class="form-group">
                                <label class="form-label">Ảnh đại diện</label>
                                <div style="display: flex; gap: 10px; align-items: center; width: 100%;">
                                    <input type="text" id="contact-form-avatar-text" class="form-control" placeholder="Chỉ cho phép các định dạng sau: .jpg, .png, .jpeg" readonly style="flex: 1;">
                                    <button class="btn btn-secondary" type="button" onclick="document.getElementById('contact-form-avatar').click()" style="height: 38px; white-space: nowrap;">Upload</button>
                                    <input type="file" id="contact-form-avatar" style="display: none;" accept=".jpg,.jpeg,.png" onchange="handleAvatarFileChange(this)">
                                </div>
                                <span id="err-avatar" style="color: #ef4444; font-size: 11px; display: none; margin-top: 4px;">Chỉ cho phép các định dạng sau: .jpg, .png, .jpeg</span>
                            </div>"""

html = html.replace(old_avatar_field, new_avatar_field)


# 5. Insert handleAvatarFileChange function to Javascript
old_validate_func = """        function validateAvatarUpload(input) {"""
new_handler_funcs = """        function handleAvatarFileChange(input) {
            const textInput = document.getElementById('contact-form-avatar-text');
            if (validateAvatarUpload(input)) {
                if (input.files && input.files[0]) {
                    textInput.value = input.files[0].name;
                }
            } else {
                textInput.value = "";
            }
        }

        function validateAvatarUpload(input) {"""

html = html.replace(old_validate_func, new_handler_funcs)

# Update reset of avatar text input in openContactFormPage
html = html.replace(
    "document.getElementById('contact-form-avatar').value = \"\";",
    "document.getElementById('contact-form-avatar').value = \"\";\n                document.getElementById('contact-form-avatar-text').value = \"\";"
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Mockup layout modifications applied successfully!")
