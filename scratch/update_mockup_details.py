import re

file_path = r"c:\Users\ManhTV\Documents\Antigravity\Gapone-Conversation\Mockup\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update css styles
style_target = """        /* Contacts View Styles */"""
style_injection = """        /* Contacts View Styles */
        .custom-select-search {
            position: relative;
            width: 100%;
        }
        .select-trigger {
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
            height: 38px;
            padding: 8px 12px;
            background: var(--bg-input);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            color: var(--text-main);
            font-size: 13px;
        }
        .select-dropdown {
            display: none;
            position: absolute;
            top: 42px;
            left: 0;
            right: 0;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            box-shadow: var(--shadow-lg);
            z-index: 150;
            padding: 8px 0;
        }
        .assignee-opt-item {
            padding: 8px 12px;
            font-size: 13px;
            color: var(--text-main);
            cursor: pointer;
        }
        .assignee-opt-item:hover {
            background-color: var(--bg-hover);
        }
"""

html = html.replace(style_target, style_injection)

# 2. Modify contacts list view (view-contacts)
# Update buttons to be right-aligned under header or in search row.
# Let's inspect where view-contacts starts and replace its HTML content.
contacts_view_target = """                <!-- VIEW: CONTACT MANAGEMENT (SRS Contact) -->
                <div id="view-contacts" class="view-panel" style="display: none; flex-direction: column; gap: 20px;">
                    <div class="settings-header" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
                        <div>
                            <h2>Danh sách liên hệ</h2>
                            <p class="settings-subtitle">Quản lý và đồng bộ thông tin liên hệ khách hàng giữa GapOne và GapOne Conversation (Shared Contact DB)</p>
                        </div>
                        <div style="display:flex; gap:10px;">
                            <button class="btn btn-secondary" onclick="showToast('Chức năng Import liên hệ sẽ được phát triển sau ở module nhập liệu.')" style="display:flex; align-items:center; gap:6px;">
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
                                Import
                            </button>
                            <button class="btn btn-secondary" onclick="openContactExportModal()" style="display:flex; align-items:center; gap:6px;">
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                                Export
                            </button>
                            <button class="btn btn-primary" onclick="openContactFormModal(null)" style="display:flex; align-items:center; gap:6px;">
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
                                Tạo Liên hệ
                            </button>
                        </div>
                    </div>

                    <!-- Search & Advanced Filter Section -->
                    <div style="display:flex; gap:16px; align-items:center; position:relative; flex-wrap:wrap; width:100%;">
                        <!-- Advanced Filter Button -->
                        <div style="position:relative;">
                            <button class="btn btn-secondary" id="adv-filter-btn" onclick="toggleAdvFilterDropdown(event)" style="display:flex; align-items:center; gap:8px;">
                                <span>Lọc nâng cao</span>
                                <svg id="adv-filter-arrow" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition:transform 0.2s;"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </button>

                            <!-- Advanced Filter Dropdown -->
                            <div class="adv-filter-dropdown" id="adv-filter-dropdown" style="display:none; position:absolute; top:45px; left:0; width:280px; background:var(--bg-card); border:1px solid var(--border-color); border-radius:8px; box-shadow:var(--shadow-lg); z-index:110; padding:8px 0;">
                                <div style="position:sticky; top:0; background:var(--bg-card); padding:8px 12px; border-bottom:1px solid var(--border-color); display:flex; align-items:center; z-index: 5;">
                                    <input type="text" id="filter-search-input" placeholder="Tìm kiếm tiêu chí..." oninput="filterCriteriaList()" style="width:100%; height:32px; border:1px solid var(--border-color); border-radius:6px; padding:0 8px; font-size:12px; background:var(--bg-input); color:var(--text-main); outline:none;">
                                </div>
                                <div id="criteria-list" style="max-height:220px; overflow-y:auto; padding:4px 0;">
                                    <!-- Populated dynamically -->
                                </div>
                            </div>
                        </div>

                        <!-- Search Box -->
                        <div class="search-container" style="flex:1; max-width:none; width:auto;">
                            <input type="text" id="contact-search-input" class="search-input" placeholder="Tìm kiếm theo tên khách hàng, email, số điện thoại..." oninput="searchContactsRealtime()">
                            <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                        </div>
                    </div>"""

contacts_view_replacement = """                <!-- VIEW: CONTACT MANAGEMENT (SRS Contact) -->
                <div id="view-contacts" class="view-panel" style="display: none; flex-direction: column; gap: 20px;">
                    <div class="settings-header">
                        <h2>Danh sách liên hệ</h2>
                        <p class="settings-subtitle">Quản lý và đồng bộ thông tin liên hệ khách hàng giữa GapOne và GapOne Conversation (Shared Contact DB)</p>
                    </div>

                    <!-- Search & Advanced Filter Section with right-aligned action buttons -->
                    <div style="display:flex; justify-content:space-between; align-items:center; position:relative; flex-wrap:wrap; width:100%; gap:16px;">
                        <div style="display:flex; gap:16px; align-items:center; flex:1; min-width: 300px; max-width: 600px;">
                            <!-- Advanced Filter Button -->
                            <div style="position:relative;">
                                <button class="btn btn-secondary" id="adv-filter-btn" onclick="toggleAdvFilterDropdown(event)" style="display:flex; align-items:center; gap:8px;">
                                    <span>Lọc nâng cao</span>
                                    <svg id="adv-filter-arrow" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition:transform 0.2s;"><polyline points="6 9 12 15 18 9"></polyline></svg>
                                </button>

                                <!-- Advanced Filter Dropdown -->
                                <div class="adv-filter-dropdown" id="adv-filter-dropdown" style="display:none; position:absolute; top:45px; left:0; width:280px; background:var(--bg-card); border:1px solid var(--border-color); border-radius:8px; box-shadow:var(--shadow-lg); z-index:110; padding:8px 0;">
                                    <div style="position:sticky; top:0; background:var(--bg-card); padding:8px 12px; border-bottom:1px solid var(--border-color); display:flex; align-items:center; z-index: 5;">
                                        <input type="text" id="filter-search-input" placeholder="Tìm kiếm tiêu chí..." oninput="filterCriteriaList()" style="width:100%; height:32px; border:1px solid var(--border-color); border-radius:6px; padding:0 8px; font-size:12px; background:var(--bg-input); color:var(--text-main); outline:none;">
                                    </div>
                                    <div id="criteria-list" style="max-height:220px; overflow-y:auto; padding:4px 0;">
                                        <!-- Populated dynamically -->
                                    </div>
                                </div>
                            </div>

                            <!-- Search Box -->
                            <div class="search-container" style="flex:1; max-width:none; width:auto; margin-bottom: 0;">
                                <input type="text" id="contact-search-input" class="search-input" placeholder="Tìm kiếm theo tên khách hàng, email, số điện thoại..." oninput="searchContactsRealtime()">
                                <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                            </div>
                        </div>

                        <!-- Right-aligned action buttons (SRS Contact Create button Right Aligned) -->
                        <div style="display:flex; gap:10px; justify-content: flex-end; align-items: center;">
                            <button class="btn btn-secondary" onclick="showToast('Chức năng Import liên hệ sẽ được phát triển sau ở module nhập liệu.')" style="display:flex; align-items:center; gap:6px;">
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
                                Import
                            </button>
                            <button class="btn btn-secondary" onclick="openContactExportModal()" style="display:flex; align-items:center; gap:6px;">
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                                Export
                            </button>
                            <button class="btn btn-primary" onclick="openContactFormPage(null)" style="display:flex; align-items:center; gap:6px;">
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
                                Tạo Liên hệ
                            </button>
                        </div>
                    </div>"""

html = html.replace(contacts_view_target, contacts_view_replacement)

# Update empty state message to "No data available" as per SRS
html = html.replace(
    '<p id="contacts-empty-message">Không có dữ liệu liên hệ</p>',
    '<p id="contacts-empty-message">No data available</p>'
)

# 3. Add view-contact-form right after view-contacts
view_contacts_end = """                        </footer>
                    </div>
                </div>"""

contact_form_view_html = """
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
                                <input type="file" id="contact-form-avatar" class="form-control" style="padding: 6px;" onchange="validateAvatarUpload(this)">
                                <span id="err-avatar" style="color: #ef4444; font-size: 11px; display: none; margin-top: 4px;">Ảnh tối đa 5MB</span>
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
                </div>"""

# Replace the closing of view-contacts to append the form view
html = html.replace(view_contacts_end, view_contacts_end + contact_form_view_html)

# 4. Remove contact-form-modal overlay from modals block
old_modal_overlay = """    <!-- Contact Form Modal (Tạo mới & Cập nhật) -->
    <div class="modal-overlay" id="contact-form-modal">
        <div class="modal-card" style="max-width: 600px;">
            <div class="modal-header">
                <h3 class="modal-title" id="contact-form-title">Liên hệ mới</h3>
                <button class="modal-close" onclick="closeContactFormModal()">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                </button>
            </div>
            <div class="modal-body" style="max-height: 420px; overflow-y: auto; padding-right: 8px;">
                <input type="hidden" id="contact-form-id">
                
                <div style="display: flex; gap: 16px; margin-bottom: 12px;">
                    <div class="form-group" style="flex: 1;">
                        <label class="form-label">Họ và tên đệm</label>
                        <input type="text" id="contact-form-lastname" class="form-control" placeholder="Nhập họ đệm" maxlength="50">
                    </div>
                    <div class="form-group" style="flex: 1;">
                        <label class="form-label">Tên *</label>
                        <input type="text" id="contact-form-firstname" class="form-control" placeholder="Nhập tên" maxlength="50">
                        <span id="err-firstname" style="color: #ef4444; font-size: 11px; display: none;">Tên là bắt buộc</span>
                    </div>
                </div>

                <div style="display: flex; gap: 16px; margin-bottom: 12px;">
                    <div class="form-group" style="flex: 1;">
                        <label class="form-label">Số điện thoại *</label>
                        <input type="text" id="contact-form-phone" class="form-control" placeholder="Nhập số điện thoại (chỉ chứa số)" maxlength="15" oninput="this.value = this.value.replace(/[^0-9]/g, '')">
                        <span id="err-phone" style="color: #ef4444; font-size: 11px; display: none;">Số điện thoại là bắt buộc</span>
                    </div>
                    <div class="form-group" style="flex: 1;">
                        <label class="form-label">Email *</label>
                        <input type="text" id="contact-form-email" class="form-control" placeholder="Nhập email" maxlength="255">
                        <span id="err-email" style="color: #ef4444; font-size: 11px; display: none;">Email là bắt buộc</span>
                    </div>
                </div>

                <div style="display: flex; gap: 16px; margin-bottom: 12px;">
                    <div class="form-group" style="flex: 1;">
                        <label class="form-label">Ngày sinh</label>
                        <input type="date" id="contact-form-dob" class="form-control" style="height: 38px;">
                    </div>
                    <div class="form-group" style="flex: 1;">
                        <label class="form-label">Giới tính</label>
                        <div style="display: flex; gap: 16px; margin-top: 10px;">
                            <label class="radio-label"><input type="radio" name="contact-gender" value="Nam" checked> Nam</label>
                            <label class="radio-label"><input type="radio" name="contact-gender" value="Nữ"> Nữ</label>
                        </div>
                    </div>
                </div>

                <div class="form-group" style="margin-bottom: 12px;">
                    <label class="form-label">Địa chỉ</label>
                    <input type="text" id="contact-form-address" class="form-control" placeholder="Nhập địa chỉ thường trú">
                </div>

                <div class="form-group" style="margin-bottom: 12px;">
                    <label class="form-label">Địa chỉ tạm trú</label>
                    <input type="text" id="contact-form-address-temp" class="form-control" placeholder="Nhập địa chỉ tạm trú" maxlength="100">
                </div>

                <div style="display: flex; gap: 16px; margin-bottom: 12px;">
                    <div class="form-group" style="flex: 1;">
                        <label class="form-label">Công ty</label>
                        <input type="text" id="contact-form-company" class="form-control" placeholder="Nhập tên công ty">
                    </div>
                    <div class="form-group" style="flex: 1;">
                        <label class="form-label">Vị trí</label>
                        <input type="text" id="contact-form-position" class="form-control" placeholder="Nhập tên chức danh/vị trí" maxlength="50">
                    </div>
                </div>

                <div style="display: flex; gap: 16px; margin-bottom: 12px;">
                    <div class="form-group" style="flex: 1;">
                        <label class="form-label">Ảnh đại diện</label>
                        <input type="file" id="contact-form-avatar" class="form-control" style="padding: 6px;" onchange="validateAvatarUpload(this)">
                        <span id="err-avatar" style="color: #ef4444; font-size: 11px; display: none;">Ảnh tối đa 5MB</span>
                    </div>
                    <div class="form-group" style="flex: 1;">
                        <label class="form-label">Sale phụ trách *</label>
                        <select id="contact-form-assignee" class="form-control" style="height: 38px;">
                            <!-- populated dynamically -->
                        </select>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" onclick="closeContactFormModal()">Hủy</button>
                <button class="btn btn-primary" onclick="saveContactForm()">Lưu</button>
            </div>
        </div>
    </div>"""

# Remove old modal from HTML
html = html.replace(old_modal_overlay, "")

# 5. Update navigateSubmenu display rules so that view-contact-form is hidden when moving to other views
# Replace:
# document.getElementById('view-contacts').style.display = 'none';
# with:
# document.getElementById('view-contacts').style.display = 'none';
# document.getElementById('view-contact-form').style.display = 'none';
html = html.replace(
    "document.getElementById('view-contacts').style.display = 'none';",
    "document.getElementById('view-contacts').style.display = 'none';\n                document.getElementById('view-contact-form').style.display = 'none';"
)

# 6. Update HTML row rendering so that row edit button calls openContactFormPage instead of openContactFormModal
html = html.replace(
    'onclick="openContactFormModal(\'${c.id}\')"',
    'onclick="openContactFormPage(\'${c.id}\')"'
)

# 7. JavaScript controller updates
# Replace the old JS functions with the new page-based controller functions.
old_js_functions = """        // CONTACT FORM MODAL (Tạo mới & Cập nhật)
        function openContactFormModal(contactId) {
            const modal = document.getElementById('contact-form-modal');
            const titleEl = document.getElementById('contact-form-title');
            const selectAssignee = document.getElementById('contact-form-assignee');
            
            // Clear validation errors
            document.getElementById('err-firstname').style.display = 'none';
            document.getElementById('err-phone').style.display = 'none';
            document.getElementById('err-email').style.display = 'none';
            document.getElementById('err-avatar').style.display = 'none';

            // Populate Sale Assignees select
            selectAssignee.innerHTML = '';
            systemUsers.forEach(u => {
                const opt = document.createElement('option');
                opt.value = u;
                opt.innerText = u;
                if (u === 'phuongntt') opt.selected = true; // default account login (SRS III)
                selectAssignee.appendChild(opt);
            });

            if (!contactId) {
                // CREATE MODE
                titleEl.innerText = "Liên hệ mới";
                document.getElementById('contact-form-id').value = "";
                document.getElementById('contact-form-lastname').value = "";
                document.getElementById('contact-form-firstname').value = "";
                document.getElementById('contact-form-phone').value = "";
                document.getElementById('contact-form-email').value = "";
                document.getElementById('contact-form-dob').value = "";
                document.querySelectorAll('input[name="contact-gender"]')[0].checked = true; // default Nam
                document.getElementById('contact-form-address').value = "";
                document.getElementById('contact-form-address-temp').value = "";
                document.getElementById('contact-form-company').value = "";
                document.getElementById('contact-form-position').value = "";
                document.getElementById('contact-form-avatar').value = "";
            } else {
                // EDIT/UPDATE MODE
                const c = contactsState.find(item => item.id === contactId);
                if (!c) return;

                titleEl.innerText = "Chỉnh sửa liên hệ";
                document.getElementById('contact-form-id').value = c.id;
                document.getElementById('contact-form-lastname').value = c.lastName || "";
                document.getElementById('contact-form-firstname').value = c.firstName || "";
                document.getElementById('contact-form-phone').value = c.phone || "";
                document.getElementById('contact-form-email').value = c.email || "";
                document.getElementById('contact-form-dob').value = c.dob || "";
                
                if (c.gender === 'Nữ') {
                    document.querySelectorAll('input[name="contact-gender"]')[1].checked = true;
                } else {
                    document.querySelectorAll('input[name="contact-gender"]')[0].checked = true;
                }
                
                document.getElementById('contact-form-address').value = c.address || "";
                document.getElementById('contact-form-address-temp').value = c.addressTemp || "";
                document.getElementById('contact-form-company').value = c.company || "";
                document.getElementById('contact-form-position').value = c.position || "";
                document.getElementById('contact-form-avatar').value = "";
                selectAssignee.value = c.assignee || "phuongntt";
            }

            modal.classList.add('open');
        }

        function closeContactFormModal() {
            document.getElementById('contact-form-modal').classList.remove('open');
        }

        function validateAvatarUpload(input) {
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
        }

        function saveContactForm() {
            const id = document.getElementById('contact-form-id').value;
            const lastName = document.getElementById('contact-form-lastname').value.trim();
            const firstName = document.getElementById('contact-form-firstname').value.trim();
            const phone = document.getElementById('contact-form-phone').value.trim();
            const email = document.getElementById('contact-form-email').value.trim();
            const dob = document.getElementById('contact-form-dob').value;
            const gender = document.querySelector('input[name="contact-gender"]:checked').value;
            const address = document.getElementById('contact-form-address').value.trim();
            const addressTemp = document.getElementById('contact-form-address-temp').value.trim();
            const company = document.getElementById('contact-form-company').value.trim();
            const position = document.getElementById('contact-form-position').value.trim();
            const assignee = document.getElementById('contact-form-assignee').value;

            // Clear errors
            document.getElementById('err-firstname').style.display = 'none';
            document.getElementById('err-phone').style.display = 'none';
            document.getElementById('err-email').style.display = 'none';

            let hasError = false;

            // Validate Tên (Required)
            if (!firstName) {
                document.getElementById('err-firstname').innerText = "Tên là bắt buộc";
                document.getElementById('err-firstname').style.display = 'block';
                hasError = true;
            }

            // Validate Số điện thoại (Required, 0-9)
            if (!phone) {
                document.getElementById('err-phone').innerText = "Số điện thoại là bắt buộc";
                document.getElementById('err-phone').style.display = 'block';
                hasError = true;
            }

            // Validate Email (Required, format)
            if (!email) {
                document.getElementById('err-email').innerText = "Email là bắt buộc";
                document.getElementById('err-email').style.display = 'block';
                hasError = true;
            } else {
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(email)) {
                    document.getElementById('err-email').innerText = "Email chưa đúng định dạng";
                    document.getElementById('err-email').style.display = 'block';
                    hasError = true;
                }
            }

            if (hasError) return;

            // Check Duplicate SĐT/Email
            const duplicatePhone = contactsState.find(c => c.phone === phone && c.id !== id);
            if (duplicatePhone) {
                document.getElementById('err-phone').innerText = "Số điện thoại đã tồn tại";
                document.getElementById('err-phone').style.display = 'block';
                return;
            }

            const duplicateEmail = contactsState.find(c => c.email === email && c.id !== id);
            if (duplicateEmail) {
                document.getElementById('err-email').innerText = "Email đã tồn tại";
                document.getElementById('err-email').style.display = 'block';
                return;
            }

            if (!id) {
                // Add new contact
                const newId = "CON-" + String(contactsState.length + 1).padStart(3, '0');
                contactsState.unshift({
                    id: newId,
                    lastName: lastName,
                    firstName: firstName,
                    phone: phone,
                    email: email,
                    dob: dob,
                    gender: gender,
                    address: address,
                    addressTemp: addressTemp,
                    company: company,
                    position: position,
                    assignee: assignee,
                    createdAt: new Date()
                });
                showToast("Tạo liên hệ thành công (Shared Contact DB)");
            } else {
                // Update contact
                const cIdx = contactsState.findIndex(c => c.id === id);
                if (cIdx > -1) {
                    contactsState[cIdx].lastName = lastName;
                    contactsState[cIdx].firstName = firstName;
                    contactsState[cIdx].phone = phone;
                    contactsState[cIdx].email = email;
                    contactsState[cIdx].dob = dob;
                    contactsState[cIdx].gender = gender;
                    contactsState[cIdx].address = address;
                    contactsState[cIdx].addressTemp = addressTemp;
                    contactsState[cIdx].company = company;
                    contactsState[cIdx].position = position;
                    contactsState[cIdx].assignee = assignee;
                    showToast("Chỉnh sửa liên hệ thành công");
                }
            }

            closeContactFormModal();
            renderContactsTable();
        }"""

new_js_functions = """        // CONTACT FORM PAGE CONTROLLER (Tạo mới & Cập nhật dạng trang)
        function openContactFormPage(contactId) {
            // Hide other view panels
            document.querySelectorAll('.view-panel').forEach(view => view.style.display = 'none');
            const viewForm = document.getElementById('view-contact-form');
            viewForm.style.display = 'flex';

            const titleEl = document.getElementById('contact-form-title');
            const subtitleEl = document.getElementById('contact-form-subtitle');
            
            // Clear validation errors
            document.getElementById('err-firstname').style.display = 'none';
            document.getElementById('err-phone').style.display = 'none';
            document.getElementById('err-email').style.display = 'none';
            document.getElementById('err-avatar').style.display = 'none';

            // Update breadcrumbs
            const parentBreadcrumb = document.getElementById('breadcrumb-parent-view');
            const breadcrumbCurrentView = document.getElementById('breadcrumb-current-view');
            if (parentBreadcrumb) parentBreadcrumb.innerText = 'Danh mục';
            
            if (!contactId) {
                // CREATE MODE
                titleEl.innerText = "Liên hệ mới";
                subtitleEl.innerText = "Tạo mới thông tin liên hệ khách hàng vào hệ thống";
                if (breadcrumbCurrentView) breadcrumbCurrentView.innerText = 'Liên hệ mới';

                document.getElementById('contact-form-id').value = "";
                document.getElementById('contact-form-lastname').value = "";
                document.getElementById('contact-form-firstname').value = "";
                document.getElementById('contact-form-phone').value = "";
                document.getElementById('contact-form-email').value = "";
                document.getElementById('contact-form-dob').value = "";
                document.querySelectorAll('input[name="contact-gender"]')[0].checked = true; // default Nam
                document.getElementById('contact-form-address').value = "";
                document.getElementById('contact-form-address-temp').value = "";
                document.getElementById('contact-form-company').value = "";
                document.getElementById('contact-form-position').value = "";
                document.getElementById('contact-form-avatar').value = "";
                
                populateAssigneeSelect('phuongntt');
            } else {
                // EDIT/UPDATE MODE
                const c = contactsState.find(item => item.id === contactId);
                if (!c) return;

                titleEl.innerText = "Chỉnh sửa liên hệ";
                subtitleEl.innerText = "Cập nhật thông tin khách hàng";
                if (breadcrumbCurrentView) breadcrumbCurrentView.innerText = 'Chỉnh sửa liên hệ';

                document.getElementById('contact-form-id').value = c.id;
                document.getElementById('contact-form-lastname').value = c.lastName || "";
                document.getElementById('contact-form-firstname').value = c.firstName || "";
                document.getElementById('contact-form-phone').value = c.phone || "";
                document.getElementById('contact-form-email').value = c.email || "";
                
                // Format Date from DB format to dd/MM/yyyy
                if (c.dob) {
                    if (c.dob.includes('-')) {
                        const parts = c.dob.split('-');
                        document.getElementById('contact-form-dob').value = parts[2] + '/' + parts[1] + '/' + parts[0];
                    } else {
                        document.getElementById('contact-form-dob').value = c.dob;
                    }
                } else {
                    document.getElementById('contact-form-dob').value = "";
                }
                
                if (c.gender === 'Nữ') {
                    document.querySelectorAll('input[name="contact-gender"]')[1].checked = true;
                } else {
                    document.querySelectorAll('input[name="contact-gender"]')[0].checked = true;
                }
                
                document.getElementById('contact-form-address').value = c.address || "";
                document.getElementById('contact-form-address-temp').value = c.addressTemp || "";
                document.getElementById('contact-form-company').value = c.company || "";
                document.getElementById('contact-form-position').value = c.position || "";
                document.getElementById('contact-form-avatar').value = "";
                
                populateAssigneeSelect(c.assignee || 'phuongntt');
            }
        }

        function closeContactFormPage() {
            document.getElementById('view-contact-form').style.display = 'none';
            navigateSubmenu('contacts');
        }

        function validateAvatarUpload(input) {
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
        }

        // Dropdown Sale phụ trách selection functions
        function populateAssigneeSelect(selectedVal = '') {
            const listContainer = document.getElementById('assignee-options-list');
            const textSpan = document.getElementById('assignee-trigger-text');
            const hiddenInput = document.getElementById('contact-form-assignee');
            const searchInput = document.getElementById('assignee-search');

            if (!listContainer) return;
            
            listContainer.innerHTML = '';
            if (searchInput) searchInput.value = '';

            const defaultVal = selectedVal || 'phuongntt';
            textSpan.innerText = defaultVal;
            hiddenInput.value = defaultVal;

            systemUsers.forEach(user => {
                const item = document.createElement('div');
                item.className = 'assignee-opt-item';
                item.innerText = user;
                item.setAttribute('data-value', user);
                item.onclick = (e) => {
                    e.stopPropagation();
                    selectAssigneeValue(user);
                };
                listContainer.appendChild(item);
            });
        }

        function selectAssigneeValue(val) {
            const textSpan = document.getElementById('assignee-trigger-text');
            const hiddenInput = document.getElementById('contact-form-assignee');
            textSpan.innerText = val;
            hiddenInput.value = val;
            closeAssigneeDropdown();
        }

        function toggleAssigneeDropdown(e) {
            e.stopPropagation();
            const dropdown = document.getElementById('assignee-select-dropdown');
            const isHidden = dropdown.style.display === 'none';
            dropdown.style.display = isHidden ? 'block' : 'none';
            if (isHidden) {
                document.getElementById('assignee-search').focus();
                filterAssigneeList();
            }
        }

        function closeAssigneeDropdown() {
            const dropdown = document.getElementById('assignee-select-dropdown');
            if (dropdown) dropdown.style.display = 'none';
        }

        function filterAssigneeList() {
            const query = document.getElementById('assignee-search').value.toLowerCase().trim();
            const listContainer = document.getElementById('assignee-options-list');
            if (!listContainer) return;

            listContainer.innerHTML = '';
            const filtered = systemUsers.filter(user => user.toLowerCase().includes(query));

            if (filtered.length === 0) {
                listContainer.innerHTML = '<div style="padding: 8px 12px; font-size: 13px; color: var(--text-muted);">Không có dữ liệu.</div>';
                return;
            }

            filtered.forEach(user => {
                const item = document.createElement('div');
                item.className = 'assignee-opt-item';
                item.innerText = user;
                item.onclick = (e) => {
                    e.stopPropagation();
                    selectAssigneeValue(user);
                };
                listContainer.appendChild(item);
            });
        }

        // Save Form Function
        function saveContactFormPage() {
            const id = document.getElementById('contact-form-id').value;
            const lastName = document.getElementById('contact-form-lastname').value.trim();
            const firstName = document.getElementById('contact-form-firstname').value.trim();
            const phone = document.getElementById('contact-form-phone').value.trim();
            const email = document.getElementById('contact-form-email').value.trim();
            const dob = document.getElementById('contact-form-dob').value.trim();
            const gender = document.querySelector('input[name="contact-gender"]:checked').value;
            const address = document.getElementById('contact-form-address').value.trim();
            const addressTemp = document.getElementById('contact-form-address-temp').value.trim();
            const company = document.getElementById('contact-form-company').value.trim();
            const position = document.getElementById('contact-form-position').value.trim();
            const assignee = document.getElementById('contact-form-assignee').value;

            // Clear errors
            document.getElementById('err-firstname').style.display = 'none';
            document.getElementById('err-phone').style.display = 'none';
            document.getElementById('err-email').style.display = 'none';

            let hasError = false;

            // Validate Tên (Required)
            if (!firstName) {
                document.getElementById('err-firstname').innerText = "Tên là bắt buộc";
                document.getElementById('err-firstname').style.display = 'block';
                hasError = true;
            }

            // Validate Số điện thoại (Required, 0-9 only)
            if (!phone) {
                document.getElementById('err-phone').innerText = "Số điện thoại là bắt buộc";
                document.getElementById('err-phone').style.display = 'block';
                hasError = true;
            }

            // Validate Email (Required, specific chars, format)
            if (!email) {
                document.getElementById('err-email').innerText = "Email là bắt buộc";
                document.getElementById('err-email').style.display = 'block';
                hasError = true;
            } else {
                const invalidChar = /[^a-z0-9\.\-@]/i;
                if (invalidChar.test(email)) {
                    document.getElementById('err-email').innerText = "Email chỉ chứa các ký tự sau: a-z, 0-9, dấu ., dấu - và @";
                    document.getElementById('err-email').style.display = 'block';
                    hasError = true;
                } else if (!email.includes('@')) {
                    document.getElementById('err-email').innerText = "Email chưa đúng định dạng";
                    document.getElementById('err-email').style.display = 'block';
                    hasError = true;
                }
            }

            if (hasError) return;

            // Check Duplicate SĐT/Email
            const duplicatePhone = contactsState.find(c => c.phone === phone && c.id !== id);
            if (duplicatePhone) {
                document.getElementById('err-phone').innerText = "Số điện thoại đã tồn tại";
                document.getElementById('err-phone').style.display = 'block';
                return;
            }

            const duplicateEmail = contactsState.find(c => c.email === email && c.id !== id);
            if (duplicateEmail) {
                document.getElementById('err-email').innerText = "Email đã tồn tại";
                document.getElementById('err-email').style.display = 'block';
                return;
            }

            // Save Date format: from dd/MM/yyyy to yyyy-MM-dd for storage
            let dobStored = dob;
            if (dob && dob.includes('/')) {
                const parts = dob.split('/');
                if (parts.length === 3) {
                    dobStored = parts[2] + '-' + parts[1] + '-' + parts[0];
                }
            }

            if (!id) {
                // Add new contact
                const newId = "CON-" + String(contactsState.length + 1).padStart(3, '0');
                contactsState.unshift({
                    id: newId,
                    lastName: lastName,
                    firstName: firstName,
                    phone: phone,
                    email: email,
                    dob: dobStored,
                    gender: gender,
                    address: address,
                    addressTemp: addressTemp,
                    company: company,
                    position: position,
                    assignee: assignee,
                    createdAt: new Date()
                });
                showToast("Tạo liên hệ thành công.");
            } else {
                // Update contact
                const cIdx = contactsState.findIndex(c => c.id === id);
                if (cIdx > -1) {
                    contactsState[cIdx].lastName = lastName;
                    contactsState[cIdx].firstName = firstName;
                    contactsState[cIdx].phone = phone;
                    contactsState[cIdx].email = email;
                    contactsState[cIdx].dob = dobStored;
                    contactsState[cIdx].gender = gender;
                    contactsState[cIdx].address = address;
                    contactsState[cIdx].addressTemp = addressTemp;
                    contactsState[cIdx].company = company;
                    contactsState[cIdx].position = position;
                    contactsState[cIdx].assignee = assignee;
                    showToast("Chỉnh sửa liên hệ thành công.");
                }
            }

            closeContactFormPage();
        }"""

html = html.replace(old_js_functions, new_js_functions)

# Close dropdowns when clicking outside
click_out_hook = """        // Initialize App
        window.addEventListener('DOMContentLoaded', () => {"""
click_out_handler = """        // Initialize App
        window.addEventListener('DOMContentLoaded', () => {
            // Register click out to close assignee custom dropdown
            window.addEventListener('click', (e) => {
                const container = document.getElementById('assignee-select-container');
                if (container && !container.contains(e.target)) {
                    closeAssigneeDropdown();
                }
            });"""

html = html.replace(click_out_hook, click_out_handler)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Mockup details updated successfully!")
