import re

file_path = r"c:\Users\ManhTV\Documents\Antigravity\Gapone-Conversation\Mockup\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Clean up duplicate views of view-contact-form.
# Let's find all occurrences of <div id="view-contact-form"
pattern = r'<!-- VIEW: CREATE / UPDATE CONTACT FORM \(SRS Contact\) -->\s*<div id="view-contact-form".*?</div>\s*</div>'
# Wait! Let's be very careful and do a precise string search and replace.
# Let's inspect the structure of the views:
# We have view-users, view-contacts, view-contact-form.
# Let's reconstruct the content-body block.
# Let's find view-users closing tag, view-contacts start and end, and place one clean view-contact-form after it.

# Let's define the single clean view-contact-form HTML
clean_contact_form_html = """
                <!-- VIEW: CREATE / UPDATE CONTACT FORM (SRS Contact) -->
                <div id="view-contact-form" class="view-panel" style="display: none; flex-direction: column; gap: 20px;">
                    <div class="settings-header">
                        <h2 id="contact-form-title">Liên hệ mới</h2>
                        <p class="settings-subtitle" id="contact-form-subtitle">Tạo mới thông tin liên hệ khách hàng vào hệ thống</p>
                    </div>

                    <div class="settings-card" style="max-width: 800px; padding: 24px;">
                        <input type="hidden" id="contact-form-id">
                        
                        <!-- Form elements -->
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
                            <div class="form-group">
                                <label class="form-label">Họ và tên đệm</label>
                                <input type="text" id="contact-form-lastname" class="form-control" placeholder="Nhập họ và tên đệm của liên hệ" maxlength="50">
                            </div>
                            <div class="form-group">
                                <label class="form-label">Tên *</label>
                                <input type="text" id="contact-form-firstname" class="form-control" placeholder="Nhập tên của liên hệ" maxlength="50">
                                <span id="err-firstname" style="color: #ef4444; font-size: 11px; display: none; margin-top: 4px;">Tên là bắt buộc</span>
                            </div>
                        </div>

                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
                            <div class="form-group">
                                <label class="form-label">Số điện thoại *</label>
                                <input type="text" id="contact-form-phone" class="form-control" placeholder="Nhập số điện thoại của liên hệ" maxlength="15" oninput="this.value = this.value.replace(/[^0-9]/g, '')">
                                <span id="err-phone" style="color: #ef4444; font-size: 11px; display: none; margin-top: 4px;">Số điện thoại là bắt buộc</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label">Email *</label>
                                <input type="text" id="contact-form-email" class="form-control" placeholder="Nhập email của liên hệ" maxlength="255">
                                <span id="err-email" style="color: #ef4444; font-size: 11px; display: none; margin-top: 4px;">Email là bắt buộc</span>
                            </div>
                        </div>

                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
                            <div class="form-group">
                                <label class="form-label">Ngày sinh</label>
                                <div style="position: relative; display: flex; align-items: center;">
                                    <input type="text" id="contact-form-dob" class="form-control" placeholder="Chọn hoặc nhập ngày sinh (dd/MM/yyyy)" maxlength="10" oninput="this.value = this.value.replace(/[^0-9\/]/g, '')" style="padding-right: 40px;">
                                    <input type="date" id="contact-form-dob-picker" style="position: absolute; right: 8px; border: none; background: transparent; cursor: pointer; width: 24px; height: 24px; opacity: 0; z-index: 2;" onchange="const val = this.value.split('-'); if(val.length===3) document.getElementById('contact-form-dob').value = val[2]+'/'+val[1]+'/'+val[0]">
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="position: absolute; right: 12px; pointer-events: none; color: var(--text-muted);"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                                </div>
                            </div>
                            <div class="form-group">
                                <label class="form-label">Giới tính</label>
                                <div style="display: flex; gap: 24px; margin-top: 10px;">
                                    <label class="radio-label"><input type="radio" name="contact-gender" value="Nam" checked> Nam</label>
                                    <label class="radio-label"><input type="radio" name="contact-gender" value="Nữ"> Nữ</label>
                                </div>
                            </div>
                        </div>

                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
                            <div class="form-group">
                                <label class="form-label">Địa chỉ</label>
                                <input type="text" id="contact-form-address" class="form-control" placeholder="Nhập địa chỉ của liên hệ">
                            </div>
                            <div class="form-group">
                                <label class="form-label">Địa chỉ tạm trú</label>
                                <input type="text" id="contact-form-address-temp" class="form-control" placeholder="Nhập địa chỉ tạm trú của liên hệ" maxlength="100">
                            </div>
                        </div>

                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
                            <div class="form-group">
                                <label class="form-label">Công ty</label>
                                <input type="text" id="contact-form-company" class="form-control" placeholder="Nhập tên công ty">
                            </div>
                            <div class="form-group">
                                <label class="form-label">Vị trí</label>
                                <input type="text" id="contact-form-position" class="form-control" placeholder="Nhập tên vị trí" maxlength="50">
                            </div>
                        </div>

                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
                            <div class="form-group">
                                <label class="form-label">Ảnh đại diện</label>
                                <span style="font-size:11px; color:var(--text-muted); display:block; margin-bottom:4px;">Chỉ cho phép các định dạng sau: .jpg, .png, .jpeg</span>
                                <input type="file" id="contact-form-avatar" class="form-control" style="padding: 6px;" accept=".jpg,.jpeg,.png" onchange="validateAvatarUpload(this)">
                                <span id="err-avatar" style="color: #ef4444; font-size: 11px; display: none; margin-top: 4px;">Chỉ cho phép các định dạng sau: .jpg, .png, .jpeg</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label">Sale phụ trách *</label>
                                <div class="custom-select-search" id="assignee-select-container" style="position: relative; width: 100%;">
                                    <div class="select-trigger form-control" onclick="toggleAssigneeDropdown(event)">
                                        <span id="assignee-trigger-text">phuongntt</span>
                                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
                                    </div>
                                    <div class="select-dropdown" id="assignee-select-dropdown">
                                        <div style="padding: 8px 12px; border-bottom: 1px solid var(--border-color); position: sticky; top: 0; background: var(--bg-card); z-index: 2;">
                                            <input type="text" id="assignee-search" class="form-control" placeholder="Search" oninput="filterAssigneeList()" onclick="event.stopPropagation()" style="height: 32px; font-size: 13px;">
                                        </div>
                                        <div id="assignee-options-list" style="max-height: 180px; overflow-y: auto;">
                                            <!-- Populated dynamically -->
                                        </div>
                                    </div>
                                </div>
                                <input type="hidden" id="contact-form-assignee">
                            </div>
                        </div>

                        <!-- Footer Actions -->
                        <div style="display: flex; justify-content: flex-end; gap: 12px; margin-top: 12px;">
                            <button class="btn btn-secondary" onclick="closeContactFormPage()">Hủy</button>
                            <button class="btn btn-primary" onclick="saveContactFormPage()">Lưu</button>
                        </div>
                    </div>
                </div>
"""

# Let's locate the views block:
# We know:
# 1. view-users ends at:
#                     </div>
#                 </div>
#                 <!-- VIEW: CREATE / UPDATE CONTACT FORM (SRS Contact) -->
# (which was the start of the first view-contact-form).
# 2. Let's find view-contacts:
#                 <!-- VIEW: CONTACT MANAGEMENT (SRS Contact) -->
#                 <div id="view-contacts" class="view-panel" style="display: none; flex-direction: column; gap: 20px;">
#                 ...
#                 </div>
# 3. Let's replace the whole sequence between view-users and view-notification-settings.
# Let's search for the start of view-contacts and get it.
# We will do a regex-based replacement or simple string splits.

content_body_start = html.find('<!-- VIEW 1: USER MANAGEMENT (Original View) -->')
notif_settings_start = html.find('<!-- VIEW 2: NOTIFICATION SETTINGS (SRS 3.4 & 4.2) -->')

if content_body_start != -1 and notif_settings_start != -1:
    before = html[:content_body_start]
    after = html[notif_settings_start:]
    
    # We want to reconstruct the content inside content-body.
    # Let's isolate view-users HTML (from content_body_start to the end of view-users).
    # We can find the exact text of view-users ending.
    view_users_html_end = html.find('<!-- VIEW: CREATE / UPDATE CONTACT FORM (SRS Contact) -->', content_body_start)
    if view_users_html_end == -1:
        # If it was named differently, search for it
        view_users_html_end = html.find('<!-- VIEW: CONTACT MANAGEMENT (SRS Contact) -->', content_body_start)
        
    view_users_content = html[content_body_start:view_users_html_end].strip()
    
    # Make sure we close the view-users div properly if needed.
    # Let's find view-contacts content
    view_contacts_idx = html.find('<!-- VIEW: CONTACT MANAGEMENT (SRS Contact) -->')
    view_contacts_end_idx = html.find('<!-- VIEW 2: NOTIFICATION SETTINGS (SRS 3.4 & 4.2) -->')
    
    # Let's get the view-contacts content specifically.
    # In index.html, view-contacts is between view_contacts_idx and the second view-contact-form.
    second_form_idx = html.find('<!-- VIEW: CREATE / UPDATE CONTACT FORM (SRS Contact) -->', view_contacts_idx)
    view_contacts_content = html[view_contacts_idx:second_form_idx].strip()
    
    # Now, reconstruct:
    # 1. view_users_content
    # 2. view_contacts_content
    # 3. clean_contact_form_html
    new_content_body = view_users_content + "\n\n" + view_contacts_content + "\n\n" + clean_contact_form_html + "\n\n                "
    
    html = before + new_content_body + after
    print("Reconstructed views cleanly and removed duplicate form panel!")

# 2. Update Javascript validation function: validateAvatarUpload
old_js_val = """        function validateAvatarUpload(input) {
            const errSpan = document.getElementById('err-avatar');
            if (input.files && input.files[0]) {
                const fileSize = input.files[0].size / 1024 / 1024; // MB
                if (fileSize > 5) {
                    errSpan.style.display = 'block';
                    input.value = ''; // Reset file
                } else {
                    errSpan.style.display = 'none';
                }
            }
        }"""

new_js_val = """        function validateAvatarUpload(input) {
            const errSpan = document.getElementById('err-avatar');
            if (input.files && input.files[0]) {
                const file = input.files[0];
                const fileSize = file.size / 1024 / 1024; // MB
                const fileName = file.name.toLowerCase();
                const allowedExtensions = ['.jpg', '.jpeg', '.png'];
                
                const isValidExtension = allowedExtensions.some(ext => fileName.endsWith(ext));
                
                if (!isValidExtension) {
                    errSpan.innerText = "Chỉ cho phép các định dạng sau: .jpg, .png, .jpeg";
                    errSpan.style.display = 'block';
                    input.value = ''; // Reset file
                    return false;
                }
                
                if (fileSize > 5) {
                    errSpan.innerText = "Ảnh tối đa 5MB";
                    errSpan.style.display = 'block';
                    input.value = ''; // Reset file
                    return false;
                }
                
                errSpan.style.display = 'none';
                return true;
            }
        }"""

html = html.replace(old_js_val, new_js_val)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated Avatar validation successfully!")
