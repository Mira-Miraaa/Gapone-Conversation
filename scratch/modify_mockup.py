import re

file_path = r"c:\Users\ManhTV\Documents\Antigravity\Gapone-Conversation\Mockup\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Inject Styles
contact_styles = """
        /* Contacts View Styles */
        .adv-filter-dropdown {
            background-color: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            box-shadow: var(--shadow-lg);
            z-index: 200;
        }
        .criteria-item {
            padding: 8px 16px;
            font-size: 13px;
            color: var(--text-main);
            cursor: pointer;
            transition: background-color 0.2s;
        }
        .criteria-item:hover {
            background-color: var(--bg-hover);
        }
        .filter-tag {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background-color: var(--primary-light);
            border: 1px solid var(--primary-border);
            color: var(--text-main);
            padding: 4px 10px;
            border-radius: 16px;
            font-size: 12px;
            font-weight: 500;
            margin-bottom: 8px;
        }
        .filter-tag-status {
            color: var(--primary-color);
            font-weight: 600;
            cursor: pointer;
            text-decoration: underline;
        }
        .filter-tag-close {
            cursor: pointer;
            color: var(--text-muted);
            font-weight: 700;
            font-size: 14px;
            display: flex;
            align-items: center;
        }
        .filter-tag-close:hover {
            color: #ef4444;
        }
        .btn-page {
            border: 1px solid var(--border-color);
            background: var(--bg-card);
            color: var(--text-main);
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 12px;
            cursor: pointer;
            font-weight: 500;
        }
        .btn-page:hover {
            background: var(--bg-hover);
        }
        .btn-page.active {
            background: var(--primary-color);
            color: white;
            border-color: var(--primary-color);
        }
        .btn-page:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }
        .tag-wrap {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 10px;
            margin-bottom: 10px;
        }
        .filter-popup-modal {
            position: absolute;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            box-shadow: var(--shadow-lg);
            padding: 16px;
            z-index: 250;
            width: 280px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        /* Style for SSO hyper-link */
        .sso-link {
            color: var(--primary-color);
            font-weight: 600;
            cursor: pointer;
            text-decoration: none;
        }
        .sso-link:hover {
            text-decoration: underline;
            color: var(--primary-hover);
        }
        /* Style for badge count on left menu if needed */
        .menu-badge {
            background-color: var(--primary-color);
            color: white;
            font-size: 10px;
            font-weight: bold;
            padding: 2px 6px;
            border-radius: 10px;
        }
"""

if contact_styles not in html:
    html = html.replace("    </style>", contact_styles + "    </style>")

# 2. Inject Left Sidebar Menu Item
menu_target = """                    <div class="menu-item" onclick="selectMenu(this)">
                        <div class="menu-item-link">
                            <span class="menu-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
                            </span>
                            <span class="menu-text">Hội thoại</span>
                        </div>
                    </div>"""

menu_replacement = menu_target + """
                    
                    <div class="menu-item" id="menu-item-contacts" onclick="navigateSubmenu('contacts')">
                        <div class="menu-item-link">
                            <span class="menu-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                            </span>
                            <span class="menu-text">Liên hệ</span>
                        </div>
                    </div>"""

html = html.replace(menu_target, menu_replacement)

# Add ID to settings menu-item
html = html.replace(
    '<div class="menu-item expanded active" onclick="toggleSubmenu(this)">',
    '<div class="menu-item expanded active" id="menu-item-settings" onclick="toggleSubmenu(this)">'
)

# 3. Inject View panel HTML
view_target = """                <!-- VIEW 2: NOTIFICATION SETTINGS (SRS 3.4 & 4.2) -->
                <div id="view-notification-settings" class="view-panel" style="display: none;">"""

contacts_html_content = """                <!-- VIEW: CONTACT MANAGEMENT (SRS Contact) -->
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
                    </div>

                    <!-- Filter Tags Container -->
                    <div id="filter-tags-container" class="tag-wrap">
                        <!-- Filter tags and clear button will render here -->
                    </div>

                    <!-- Contacts Table Card -->
                    <div class="table-card" style="flex:1; display:flex; flex-direction:column; min-height:400px;">
                        <div class="table-responsive" style="flex:1; overflow-y:auto; overflow-x:auto; max-height: 500px;">
                            <table id="contacts-table">
                                <thead style="position:sticky; top:0; z-index: 2;">
                                    <tr>
                                        <th class="col-stt">STT</th>
                                        <th style="cursor:pointer;" onclick="sortContacts('id')">ID <span id="sort-icon-id" style="font-size:10px; margin-left:4px; color:var(--primary-color);"></span></th>
                                        <th style="cursor:pointer;" onclick="sortContacts('name')">Họ và tên <span id="sort-icon-name" style="font-size:10px; margin-left:4px; color:var(--primary-color);"></span></th>
                                        <th style="cursor:pointer;" onclick="sortContacts('email')">Email <span id="sort-icon-email" style="font-size:10px; margin-left:4px; color:var(--primary-color);"></span></th>
                                        <th style="cursor:pointer;" onclick="sortContacts('phone')">Số điện thoại <span id="sort-icon-phone" style="font-size:10px; margin-left:4px; color:var(--primary-color);"></span></th>
                                        <th>Ngày sinh</th>
                                        <th>Địa chỉ</th>
                                        <th style="cursor:pointer;" onclick="sortContacts('createdAt')">Ngày tạo <span id="sort-icon-createdAt" style="font-size:10px; margin-left:4px; color:var(--primary-color);"></span></th>
                                        <th class="col-actions">Hành động</th>
                                    </tr>
                                </thead>
                                <tbody id="contacts-table-body">
                                    <!-- Populated dynamically -->
                                </tbody>
                            </table>
                            <div class="empty-state" id="contacts-empty-state" style="display:none;">
                                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                                <p id="contacts-empty-message">Không có dữ liệu liên hệ</p>
                            </div>
                        </div>
                        <footer class="footer-section">
                            <div style="display:flex; justify-content:space-between; width:100%; align-items:center; flex-wrap:wrap; gap:10px;">
                                <div style="font-size:12px; color:var(--text-muted);" id="contact-pagination-info">
                                    Hiển thị 1-10 trên 100 bản ghi
                                </div>
                                <div class="pagination-container">
                                    <span style="font-size:12px; color:var(--text-muted);">Số bản ghi/trang:</span>
                                    <select class="page-size-selector" id="contact-page-size" onchange="changeContactPageSize(this.value)">
                                        <option value="10">10</option>
                                        <option value="25" selected>25</option>
                                        <option value="50">50</option>
                                        <option value="100">100</option>
                                    </select>
                                    <div style="display:flex; gap:4px;" id="contact-pages-btn">
                                        <!-- Pagination buttons -->
                                    </div>
                                </div>
                            </div>
                        </footer>
                    </div>
                </div>
"""

html = html.replace(view_target, contacts_html_content + view_target)

# 4. Inject Modals HTML
modals_target = "    <!-- Dynamic Toasts Stack (SRS Toast Queue 3.2) -->"

contact_modals_html = """
    <!-- Contact Form Modal (Tạo mới & Cập nhật) -->
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
    </div>

    <!-- Contact Delete Confirmation Modal -->
    <div class="modal-overlay" id="contact-delete-modal">
        <div class="modal-card" style="max-width: 400px;">
            <div class="modal-header">
                <h3 class="modal-title">Xóa liên hệ</h3>
                <button class="modal-close" onclick="closeContactDeleteModal()">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                </button>
            </div>
            <div class="modal-body">
                <input type="hidden" id="contact-delete-id">
                <p style="font-size: 14px; color: var(--text-main); text-align: left;">Bạn có chắc muốn xóa liên hệ này?</p>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" onclick="closeContactDeleteModal()">Hủy</button>
                <button class="btn btn-primary" onclick="confirmDeleteContact()" style="background-color: #ef4444; border-color: #ef4444;">Đồng ý</button>
            </div>
        </div>
    </div>

    <!-- Contact Export Excel Modal -->
    <div class="modal-overlay" id="contact-export-modal">
        <div class="modal-card" style="max-width: 450px;">
            <div class="modal-header">
                <h3 class="modal-title">Xuất file Excel danh sách khách hàng</h3>
                <button class="modal-close" onclick="closeContactExportModal()">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                </button>
            </div>
            <div class="modal-body" style="text-align: left;">
                <p style="font-weight: 600; font-size: 14px; margin-bottom: 12px;">Dữ liệu sẽ được trích xuất:</p>
                <div style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 20px;">
                    <label class="radio-label" style="font-size:14px; font-weight: 500;">
                        <input type="radio" name="export-scope" value="filter" checked onclick="toggleExportScopeWarning(false)"> Theo kết quả bộ lọc hiện tại
                    </label>
                    <label class="radio-label" style="font-size:14px; font-weight: 500;">
                        <input type="radio" name="export-scope" value="page" onclick="toggleExportScopeWarning(false)"> Theo trang hiện tại
                    </label>
                    <label class="radio-label" style="font-size:14px; font-weight: 500;">
                        <input type="radio" name="export-scope" value="all" onclick="toggleExportScopeWarning(true)"> Theo toàn bộ danh sách
                    </label>
                </div>
                
                <div id="export-scope-warning" style="display: none; background-color: #fffbeb; border: 1px solid #fef3c7; color: #b45309; padding: 10px 14px; border-radius: 6px; font-size: 12px; margin-bottom: 16px;">
                    Nếu xuất toàn bộ danh sách thì file sẽ tốn nhiều thời gian xử lý hơn bình thường.
                </div>

                <div style="background-color: var(--bg-hover); padding: 12px; border-radius: 8px; font-size: 12px; color: var(--text-muted); display:flex; flex-direction:column; gap:6px; border: 1px solid var(--border-color);">
                    <div style="display: flex; gap: 6px; align-items: flex-start;">
                        <span style="color: var(--primary-color); font-weight: bold;">i</span>
                        <span>File Excel sẽ được xử lý và sẵn sàng tải tại <strong>Cài đặt → Quản lý xuất dữ liệu</strong>.</span>
                    </div>
                    <div style="display: flex; gap: 6px; align-items: flex-start;">
                        <span style="color: var(--primary-color); font-weight: bold;">i</span>
                        <span>Thứ tự cột trong file Excel được sắp xếp theo mục <strong>Cài đặt → Thuộc tính</strong>.</span>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" onclick="closeContactExportModal()">Cancel</button>
                <button class="btn btn-primary" onclick="submitContactExport()">Export Excel</button>
            </div>
        </div>
    </div>

    <!-- SSO MOCK LANDING PAGE MODAL -->
    <div class="modal-overlay" id="sso-profile-modal" style="background-color: rgba(15,15,16,0.95); z-index: 1000;">
        <div class="modal-card" style="max-width: 900px; height: 90vh; display: flex; flex-direction: column;">
            <div class="modal-header" style="background: linear-gradient(135deg, #f06a24, #d35515); color: white; border: none; padding: 16px 24px;">
                <h3 class="modal-title" style="color: white; display: flex; align-items: center; gap: 10px;">
                    <span style="background: white; color: #f06a24; border-radius: 50%; width: 24px; height: 24px; display: inline-flex; align-items: center; justify-content: center; font-weight: bold; font-size: 14px;">GO</span>
                    Cổng Thông Tin GapOne Portal (Đã đăng nhập qua SSO chéo - AC3)
                </h3>
                <button class="modal-close" onclick="closeSsoProfileModal()" style="color: white; filter: brightness(2);">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                </button>
            </div>
            <div class="modal-body" id="sso-profile-body" style="flex:1; overflow-y:auto; padding:24px; background: var(--bg-main); text-align: left;">
                <!-- Filled by JS -->
            </div>
            <div class="modal-footer" style="background-color: var(--bg-sidebar); border-top: 1px solid var(--border-color);">
                <button class="btn btn-primary" onclick="closeSsoProfileModal()">Đóng cửa sổ SSO</button>
            </div>
        </div>
    </div>
"""

html = html.replace(modals_target, contact_modals_html + modals_target)

# 5. Inject Script Navigation modifications
nav_search = """        function navigateSubmenu(viewName) {
            document.querySelectorAll('.submenu-item').forEach(item => item.classList.remove('active'));
            const parentBreadcrumb = document.getElementById('breadcrumb-parent-view');"""

nav_replacement = """        function navigateSubmenu(viewName) {
            document.querySelectorAll('.submenu-item').forEach(item => item.classList.remove('active'));
            const parentBreadcrumb = document.getElementById('breadcrumb-parent-view');
            
            // Manage active state of sidebar menu item (especially Contacts)
            const menuSettings = document.getElementById('menu-item-settings');
            const menuContacts = document.getElementById('menu-item-contacts');
            if (viewName === 'contacts') {
                if (menuSettings) {
                    menuSettings.classList.remove('active');
                    menuSettings.style.color = '';
                    const icon = menuSettings.querySelector('.menu-icon');
                    if (icon) icon.style.color = '';
                    const submenu = document.getElementById('settings-submenu');
                    if (submenu) submenu.classList.remove('expanded');
                    menuSettings.classList.remove('expanded');
                }
                if (menuContacts) {
                    menuContacts.classList.add('active');
                    menuContacts.style.color = 'var(--primary-color)';
                    const icon = menuContacts.querySelector('.menu-icon');
                    if (icon) icon.style.color = 'var(--primary-color)';
                }
            } else {
                if (menuContacts) {
                    menuContacts.classList.remove('active');
                    menuContacts.style.color = '';
                    const icon = menuContacts.querySelector('.menu-icon');
                    if (icon) icon.style.color = '';
                }
                if (menuSettings) {
                    menuSettings.classList.add('active');
                    menuSettings.classList.add('expanded');
                    menuSettings.style.color = 'var(--primary-color)';
                    const icon = menuSettings.querySelector('.menu-icon');
                    if (icon) icon.style.color = 'var(--primary-color)';
                    const submenu = document.getElementById('settings-submenu');
                    if (submenu) submenu.classList.add('expanded');
                }
            }"""

html = html.replace(nav_search, nav_replacement)

# Also handle the display logic inside `navigateSubmenu`
nav_views_search = """            if (viewName === 'users') {
                document.getElementById('sub-menu-users').classList.add('active');
                viewUsers.style.display = 'flex';
                viewNotifSettings.style.display = 'none';
                viewChannels.style.display = 'none';
                if (parentBreadcrumb) parentBreadcrumb.innerText = 'Cài đặt';
                breadcrumbCurrentView.innerText = 'Người dùng';"""

nav_views_replacement = """            if (viewName === 'contacts') {
                viewUsers.style.display = 'none';
                viewNotifSettings.style.display = 'none';
                viewChannels.style.display = 'none';
                document.getElementById('view-contacts').style.display = 'flex';
                if (parentBreadcrumb) parentBreadcrumb.innerText = 'Danh mục';
                breadcrumbCurrentView.innerText = 'Liên hệ';
                renderContactsTable();
            } else {
                document.getElementById('view-contacts').style.display = 'none';
            }
            
            if (viewName === 'users') {
                document.getElementById('sub-menu-users').classList.add('active');
                viewUsers.style.display = 'flex';
                viewNotifSettings.style.display = 'none';
                viewChannels.style.display = 'none';
                if (parentBreadcrumb) parentBreadcrumb.innerText = 'Cài đặt';
                breadcrumbCurrentView.innerText = 'Người dùng';"""

html = html.replace(nav_search + "\n" + nav_views_search, nav_replacement + "\n" + nav_views_replacement)

# Make sure other view changes clean up view-contacts
html = html.replace(
    "            } else if (viewName === 'channels') {",
    "                document.getElementById('view-contacts').style.display = 'none';\n            } else if (viewName === 'channels') {"
)
html = html.replace(
    "            } else if (viewName === 'notif-settings') {",
    "                document.getElementById('view-contacts').style.display = 'none';\n            } else if (viewName === 'notif-settings') {"
)

# 6. Inject Contacts Javascript Logic
js_target = "        // VIEW NAVIGATION & MAIN SWITCHERS"

contacts_js_logic = """
        // ========================================================================================
        // JS LOGIC FOR CONTACT MANAGEMENT (SRS CONTACT)
        // ========================================================================================

        // Contacts list database
        let contactsState = [
            { id: "CON-001", lastName: "Nguyễn Văn", firstName: "An", email: "an.nv@gapit.com.vn", phone: "0912345678", dob: "1990-05-12", gender: "Nam", address: "Hà Nội", addressTemp: "Thanh Xuân, Hà Nội", company: "Gapit Media", position: "Developer", assignee: "phuongntt", createdAt: new Date("2026-06-01 08:30") },
            { id: "CON-002", lastName: "Trần Thị", firstName: "Bình", email: "binh.tt@gmail.com", phone: "0987654321", dob: "1993-09-24", gender: "Nữ", address: "Hải Phòng", addressTemp: "Cầu Giấy, Hà Nội", company: "FPT", position: "QC Engineer", assignee: "duyennt", createdAt: new Date("2026-06-15 14:20"), hasOrders: true },
            { id: "CON-003", lastName: "Lê Hoàng", firstName: "Cường", email: "cuong.lh@yahoo.com", phone: "0904445556", dob: "1988-12-05", gender: "Nam", address: "Đà Nẵng", addressTemp: "Đà Nẵng", company: "Viettel", position: "Project Manager", assignee: "khanhhn_gapone", createdAt: new Date("2026-06-20 10:15") },
            { id: "CON-004", lastName: "Phạm Minh", firstName: "Dương", email: "duong.pm@gapit.com.vn", phone: "0936667778", dob: "1995-02-18", gender: "Nam", address: "Hồ Chí Minh", addressTemp: "Bình Thạnh, HCM", company: "Gapit Tech", position: "Designer", assignee: "phuongntt", createdAt: new Date("2026-06-25 16:45") },
            { id: "CON-005", lastName: "Hoàng Thu", firstName: "Giang", email: "giang.ht@outlook.com", phone: "0975558889", dob: "1992-07-30", gender: "Nữ", address: "Cần Thơ", addressTemp: "Ba Đình, Hà Nội", company: "Vingroup", position: "Data Analyst", assignee: "uyendtt", createdAt: new Date("2026-06-28 09:00") },
            { id: "CON-006", lastName: "Vũ Hải", firstName: "Đăng", email: "dang.vh@gmail.com", phone: "0949991112", dob: "1991-03-14", gender: "Nam", address: "Ninh Bình", addressTemp: "Nam Từ Liêm, HN", company: "MobiFone", position: "Sales Manager", assignee: "hungbm", createdAt: new Date("2026-06-29 11:30") },
            { id: "CON-007", lastName: "Đỗ Thị", firstName: "Hồng", email: "hong.dt@gmail.com", phone: "0918882223", dob: "1994-11-22", gender: "Nữ", address: "Nam Định", addressTemp: "Đống Đa, Hà Nội", company: "Techcombank", position: "Accountant", assignee: "gapone_sp", createdAt: new Date("2026-06-30 15:10") }
        ];

        // System users for Assignee dropdown
        const systemUsers = ["phuongntt", "duyennt", "khanhhn_gapone", "uyendtt", "hungbm", "gapone_sp"];

        // Pagination and Sorting states
        let contactPageSize = 25;
        let contactCurrentPage = 1;
        let contactSortField = 'createdAt';
        let contactSortOrder = 'desc'; // 'asc' or 'desc'

        // Advanced filter search criteria
        const filterCriteria = [
            { field: 'name', name: 'Họ và tên', type: 'text' },
            { field: 'email', name: 'Email', type: 'text' },
            { field: 'phone', name: 'Số điện thoại', type: 'number' },
            { field: 'dob', name: 'Ngày sinh', type: 'date' },
            { field: 'address', name: 'Địa chỉ', type: 'text' },
            { field: 'company', name: 'Công ty', type: 'text' },
            { field: 'position', name: 'Vị trí', type: 'text' },
            { field: 'assignee', name: 'Sale phụ trách', type: 'dropdown', options: systemUsers },
            { field: 'createdAt', name: 'Ngày tạo', type: 'date' }
        ];

        // Active filters list
        let activeFilters = []; // { field, value, operator, label }

        // Render functions
        function renderContactsTable() {
            const tbody = document.getElementById('contacts-table-body');
            const emptyState = document.getElementById('contacts-empty-state');
            if (!tbody) return;
            tbody.innerHTML = '';

            // Apply Search & Filters
            let filtered = [...contactsState];

            // 1. Main Text Search (OR operator on name, email, phone)
            const searchQuery = document.getElementById('contact-search-input').value.toLowerCase().trim();
            if (searchQuery) {
                filtered = filtered.filter(c => {
                    const fullName = ((c.lastName || '') + ' ' + (c.firstName || '')).toLowerCase();
                    const email = (c.email || '').toLowerCase();
                    const phone = (c.phone || '');
                    return fullName.includes(searchQuery) || email.includes(searchQuery) || phone.includes(searchQuery);
                });
            }

            // 2. Advanced Filters (OR operator across different fields as per SRS)
            if (activeFilters.length > 0) {
                filtered = filtered.filter(c => {
                    // Check if contact matches ANY of the filters (OR logic)
                    let matchedAny = false;
                    for (let f of activeFilters) {
                        if (f.operator === 'Chưa lọc') continue;

                        let val = '';
                        if (f.field === 'name') {
                            val = ((c.lastName || '') + ' ' + (c.firstName || '')).toLowerCase();
                        } else if (f.field === 'createdAt') {
                            // Date format dd/MM/yyyy
                            const dateObj = c.createdAt;
                            val = `${String(dateObj.getDate()).padStart(2,'0')}/${String(dateObj.getMonth()+1).padStart(2,'0')}/${dateObj.getFullYear()}`;
                        } else {
                            val = (c[f.field] || '').toString().toLowerCase();
                        }

                        let targetVal = (f.value || '').toString().toLowerCase();

                        // Operator calculations
                        if (f.operator === 'Có dữ liệu') {
                            if (val && val.trim() !== '') matchedAny = true;
                        } else if (f.operator === 'Không có dữ liệu') {
                            if (!val || val.trim() === '') matchedAny = true;
                        } else if (f.operator === 'Bằng') {
                            if (val === targetVal) matchedAny = true;
                        } else if (f.operator === 'Không bằng') {
                            if (val !== targetVal) matchedAny = true;
                        } else if (f.operator === 'Chứa giá trị') {
                            if (val.includes(targetVal)) matchedAny = true;
                        } else if (f.operator === 'Không chứa giá trị') {
                            if (!val.includes(targetVal)) matchedAny = true;
                        } else if (f.operator === 'Bắt đầu bằng') {
                            if (val.startsWith(targetVal)) matchedAny = true;
                        } else if (f.operator === 'Kết thúc bằng') {
                            if (val.endsWith(targetVal)) matchedAny = true;
                        } else if (f.operator === 'Lớn hơn') {
                            if (parseFloat(val) > parseFloat(targetVal)) matchedAny = true;
                        } else if (f.operator === 'Nhỏ hơn') {
                            if (parseFloat(val) < parseFloat(targetVal)) matchedAny = true;
                        } else if (f.operator === 'Lớn hơn hoặc bằng') {
                            if (parseFloat(val) >= parseFloat(targetVal)) matchedAny = true;
                        } else if (f.operator === 'Nhỏ hơn hoặc bằng') {
                            if (parseFloat(val) <= parseFloat(targetVal)) matchedAny = true;
                        } else if (f.operator === 'Trong khoảng') {
                            if (f.field === 'dob' || f.field === 'createdAt') {
                                // Date range
                                const [d1, d2] = targetVal.split('~');
                                const curDate = new Date(c[f.field]);
                                if (curDate >= new Date(d1) && curDate <= new Date(d2)) matchedAny = true;
                            } else {
                                const [v1, v2] = targetVal.split('~');
                                const num = parseFloat(val);
                                if (num >= parseFloat(v1) && num <= parseFloat(v2)) matchedAny = true;
                            }
                        } else if (f.operator === 'Ngoài khoảng') {
                            const [v1, v2] = targetVal.split('~');
                            const num = parseFloat(val);
                            if (num < parseFloat(v1) || num > parseFloat(v2)) matchedAny = true;
                        } else if (f.operator === 'Trước' || f.operator === 'Trước thời điểm') {
                            if (new Date(c[f.field]) < new Date(targetVal)) matchedAny = true;
                        } else if (f.operator === 'Sau' || f.operator === 'Sau thời điểm') {
                            if (new Date(c[f.field]) > new Date(targetVal)) matchedAny = true;
                        }
                    }
                    return matchedAny;
                });
            }

            // 3. Sorting
            filtered.sort((a, b) => {
                let valA = a[contactSortField];
                let valB = b[contactSortField];

                if (contactSortField === 'name') {
                    valA = ((a.lastName || '') + ' ' + (a.firstName || '')).toLowerCase();
                    valB = ((b.lastName || '') + ' ' + (b.firstName || '')).toLowerCase();
                }

                if (valA < valB) return contactSortOrder === 'asc' ? -1 : 1;
                if (valA > valB) return contactSortOrder === 'asc' ? 1 : -1;
                return 0;
            });

            // Update Header Sort Icons
            const fieldsToSort = ['id', 'name', 'email', 'phone', 'createdAt'];
            fieldsToSort.forEach(f => {
                const span = document.getElementById(`sort-icon-${f}`);
                if (span) {
                    if (contactSortField === f) {
                        span.innerText = contactSortOrder === 'asc' ? '▲' : '▼';
                    } else {
                        span.innerText = '';
                    }
                }
            });

            // 4. Pagination
            const totalRecords = filtered.length;
            const totalPages = Math.ceil(totalRecords / contactPageSize) || 1;
            if (contactCurrentPage > totalPages) contactCurrentPage = totalPages;
            
            const startIndex = (contactCurrentPage - 1) * contactPageSize;
            const endIndex = Math.min(startIndex + contactPageSize, totalRecords);
            const pagedData = filtered.slice(startIndex, endIndex);

            // Update Pagination info
            const pagInfo = document.getElementById('contact-pagination-info');
            if (pagInfo) {
                if (totalRecords === 0) {
                    pagInfo.innerText = 'Hiển thị 0-0 trên 0 bản ghi';
                } else {
                    pagInfo.innerText = `Hiển thị ${startIndex + 1}-${endIndex} trên ${totalRecords} bản ghi`;
                }
            }

            // Render Rows
            if (totalRecords === 0) {
                emptyState.style.display = 'block';
                document.getElementById('contacts-table').style.display = 'none';
            } else {
                emptyState.style.display = 'none';
                document.getElementById('contacts-table').style.display = 'table';
                
                pagedData.forEach((c, idx) => {
                    const row = document.createElement('tr');
                    row.setAttribute('data-contact-id', c.id);
                    
                    const stt = startIndex + idx + 1;
                    const fullName = (c.lastName || '') + ' ' + (c.firstName || '');
                    
                    // Format date
                    const dateObj = c.createdAt;
                    const dateString = `${String(dateObj.getDate()).padStart(2,'0')}/${String(dateObj.getMonth()+1).padStart(2,'0')}/${dateObj.getFullYear()} ${String(dateObj.getHours()).padStart(2,'0')}:${String(dateObj.getMinutes()).padStart(2,'0')}`;
                    
                    const dobFormatted = c.dob ? c.dob.split('-').reverse().join('/') : '−';

                    row.innerHTML = `
                        <td class="col-stt">${stt}</td>
                        <td><span class="sso-link" onclick="openSsoProfile('${c.id}')">${c.id}</span></td>
                        <td><span class="sso-link" onclick="openSsoProfile('${c.id}')">${fullName}</span></td>
                        <td>${c.email || '−'}</td>
                        <td>${c.phone || '−'}</td>
                        <td>${dobFormatted}</td>
                        <td style="max-width: 150px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;" title="${c.address || ''}">${c.address || '−'}</td>
                        <td>${dateString}</td>
                        <td class="col-actions" style="display:flex; gap:6px; justify-content:center;">
                            <button class="btn-action" onclick="openContactFormModal('${c.id}')" title="Sửa thông tin">
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 1 1 3 3L12 15l-4 1 1-4z"></path></svg>
                            </button>
                            <button class="btn-action" onclick="openContactDeleteModal('${c.id}')" title="Xóa" style="color:#ef4444; background-color:rgba(239, 68, 68, 0.05); border-color:rgba(239, 68, 68, 0.15);">
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path><line x1="10" y1="11" x2="10" y2="17"></line><line x1="14" y1="11" x2="14" y2="17"></line></svg>
                            </button>
                        </td>
                    `;
                    tbody.appendChild(row);
                });
            }

            // Render Pagination buttons
            renderContactPaginationButtons(totalPages);
            renderFilterTags();
        }

        function renderContactPaginationButtons(totalPages) {
            const container = document.getElementById('contact-pages-btn');
            if (!container) return;
            container.innerHTML = '';

            // Previous Button
            const prevBtn = document.createElement('button');
            prevBtn.className = 'btn-page';
            prevBtn.innerText = '‹';
            prevBtn.disabled = contactCurrentPage === 1;
            prevBtn.onclick = () => {
                contactCurrentPage--;
                renderContactsTable();
            };
            container.appendChild(prevBtn);

            // Page Numbers
            for (let i = 1; i <= totalPages; i++) {
                const pageBtn = document.createElement('button');
                pageBtn.className = `btn-page ${contactCurrentPage === i ? 'active' : ''}`;
                pageBtn.innerText = i;
                pageBtn.onclick = () => {
                    contactCurrentPage = i;
                    renderContactsTable();
                };
                container.appendChild(pageBtn);
            }

            // Next Button
            const nextBtn = document.createElement('button');
            nextBtn.className = 'btn-page';
            nextBtn.innerText = '›';
            nextBtn.disabled = contactCurrentPage === totalPages;
            nextBtn.onclick = () => {
                contactCurrentPage++;
                renderContactsTable();
            };
            container.appendChild(nextBtn);
        }

        // Sorting Logic
        function sortContacts(field) {
            if (contactSortField === field) {
                contactSortOrder = contactSortOrder === 'asc' ? 'desc' : 'asc';
            } else {
                contactSortField = field;
                contactSortOrder = 'asc';
            }
            renderContactsTable();
            showToast(`Sắp xếp danh sách theo ${field === 'name' ? 'Họ và tên' : field.toUpperCase()} (${contactSortOrder === 'asc' ? 'A-Z' : 'Z-A'})`);
        }

        // Realtime Search with Debouncing (SRS 3.2 logic / real-time search)
        function searchContactsRealtime() {
            contactCurrentPage = 1; // reset page
            renderContactsTable();
        }

        // Change Page size
        function changeContactPageSize(val) {
            contactPageSize = parseInt(val, 10);
            contactCurrentPage = 1;
            renderContactsTable();
            showToast(`Hiển thị ${val} dòng mỗi trang`);
        }

        // ADVANCED FILTER LOGIC (SRS II)
        function toggleAdvFilterDropdown(e) {
            e.stopPropagation();
            const dropdown = document.getElementById('adv-filter-dropdown');
            const arrow = document.getElementById('adv-filter-arrow');
            const isHidden = dropdown.style.display === 'none';
            
            dropdown.style.display = isHidden ? 'block' : 'none';
            if (arrow) {
                arrow.style.transform = isHidden ? 'rotate(180deg)' : '';
            }
            if (isHidden) {
                populateCriteriaList();
                document.getElementById('filter-search-input').focus();
            }
        }

        function filterCriteriaList() {
            const query = document.getElementById('filter-search-input').value.toLowerCase().trim();
            populateCriteriaList(query);
        }

        function populateCriteriaList(query = '') {
            const container = document.getElementById('criteria-list');
            if (!container) return;
            container.innerHTML = '';

            const filtered = filterCriteria.filter(c => c.name.toLowerCase().includes(query));

            if (filtered.length === 0) {
                container.innerHTML = '<div style="padding:8px 12px; font-size:12px; color:var(--text-muted);">Không có tiêu chí phù hợp</div>';
                return;
            }

            filtered.forEach(c => {
                const div = document.createElement('div');
                div.className = 'criteria-item';
                div.innerText = c.name;
                div.onclick = (e) => {
                    e.stopPropagation();
                    addFilterTag(c.field);
                    document.getElementById('adv-filter-dropdown').style.display = 'none';
                    const arrow = document.getElementById('adv-filter-arrow');
                    if (arrow) arrow.style.transform = '';
                };
                container.appendChild(div);
            });
        }

        function addFilterTag(field) {
            // Check if filter for this field already exists
            const existing = activeFilters.find(f => f.field === field);
            if (existing) {
                showToast(`Tiêu chí "${existing.label}" đã được thêm.`);
                return;
            }

            const schema = filterCriteria.find(c => c.field === field);
            if (schema) {
                activeFilters.push({
                    field: field,
                    label: schema.name,
                    operator: 'Chưa lọc',
                    value: '',
                    type: schema.type,
                    options: schema.options || null
                });
                renderContactsTable();
            }
        }

        function renderFilterTags() {
            const container = document.getElementById('filter-tags-container');
            if (!container) return;
            container.innerHTML = '';

            if (activeFilters.length === 0) {
                container.style.display = 'none';
                return;
            }
            container.style.display = 'flex';

            activeFilters.forEach((f, idx) => {
                const tag = document.createElement('div');
                tag.className = 'filter-tag';
                
                let valuePreview = '';
                if (f.operator !== 'Chưa lọc' && f.operator !== 'Có dữ liệu' && f.operator !== 'Không có dữ liệu') {
                    if (f.value) {
                        valuePreview = `: ${f.operator} "${f.value}"`;
                    }
                } else if (f.operator === 'Có dữ liệu' || f.operator === 'Không có dữ liệu') {
                    valuePreview = `: ${f.operator}`;
                } else {
                    valuePreview = ': Chưa lọc';
                }

                tag.innerHTML = `
                    <span>${f.label}</span>
                    <span class="filter-tag-status" onclick="openFilterConfigPopup(event, ${idx})">${valuePreview}</span>
                    <span class="filter-tag-close" onclick="removeFilterTag(event, ${idx})">×</span>
                `;
                container.appendChild(tag);
            });

            // Add clear all button
            const clearBtn = document.createElement('button');
            clearBtn.className = 'btn btn-secondary';
            clearBtn.style = 'border-radius: 16px; font-size:12px; padding: 4px 12px; height: auto;';
            clearBtn.innerText = 'Xóa bộ lọc';
            clearBtn.onclick = () => {
                activeFilters = [];
                renderContactsTable();
                showToast('Đã xóa tất cả bộ lọc nâng cao');
            };
            container.appendChild(clearBtn);
        }

        function removeFilterTag(e, idx) {
            e.stopPropagation();
            activeFilters.splice(idx, 1);
            renderContactsTable();
        }

        // Configuration details popup
        let activeConfigPopup = null;

        function openFilterConfigPopup(e, idx) {
            e.stopPropagation();
            
            // Close any open popup
            closeFilterConfigPopup();

            const filter = activeFilters[idx];
            const tagRect = e.target.getBoundingClientRect();

            const popup = document.createElement('div');
            popup.className = 'filter-popup-modal';
            popup.id = 'filter-config-popup';
            
            // Position popup below tag
            popup.style.position = 'absolute';
            popup.style.top = (tagRect.bottom + window.scrollY + 8) + 'px';
            popup.style.left = (tagRect.left + window.scrollX) + 'px';

            // Operators based on type
            let operators = [];
            if (filter.type === 'text') {
                operators = ['Bằng', 'Không bằng', 'Chứa giá trị', 'Không chứa giá trị', 'Bắt đầu bằng', 'Kết thúc bằng', 'Có dữ liệu', 'Không có dữ liệu'];
            } else if (filter.type === 'number') {
                operators = ['Bằng', 'Không bằng', 'Lớn hơn', 'Nhỏ hơn', 'Lớn hơn hoặc bằng', 'Nhỏ hơn hoặc bằng', 'Trong khoảng', 'Ngoài khoảng', 'Có dữ liệu', 'Không có dữ liệu'];
            } else if (filter.type === 'date') {
                operators = ['Trong khoảng', 'Trước thời điểm', 'Sau thời điểm', 'Có dữ liệu', 'Không có dữ liệu'];
            } else if (filter.type === 'dropdown') {
                operators = ['Bằng', 'Không bằng', 'Có dữ liệu', 'Không có dữ liệu'];
            }

            let optHtml = operators.map(op => `<option value="${op}" ${filter.operator === op ? 'selected' : ''}>${op}</option>`).join('');

            // Value Input element based on type and operator
            let valueInputHtml = '';
            if (filter.operator === 'Có dữ liệu' || filter.operator === 'Không có dữ liệu') {
                valueInputHtml = `<input type="text" id="popup-val-input" class="form-control" style="height:32px;" disabled placeholder="Không cần nhập giá trị">`;
            } else if (filter.operator === 'Trong khoảng' || filter.operator === 'Ngoài khoảng') {
                if (filter.type === 'date') {
                    const [d1, d2] = (filter.value || '').split('~');
                    valueInputHtml = `
                        <div style="display:flex; flex-direction:column; gap:6px;">
                            <input type="date" id="popup-val-date1" class="form-control" style="height:32px;" value="${d1 || ''}">
                            <input type="date" id="popup-val-date2" class="form-control" style="height:32px;" value="${d2 || ''}">
                        </div>
                    `;
                } else {
                    const [v1, v2] = (filter.value || '').split('~');
                    valueInputHtml = `
                        <div style="display:flex; gap:6px;">
                            <input type="number" id="popup-val-num1" class="form-control" style="height:32px; flex:1;" value="${v1 || ''}" placeholder="Từ">
                            <input type="number" id="popup-val-num2" class="form-control" style="height:32px; flex:1;" value="${v2 || ''}" placeholder="Đến">
                        </div>
                    `;
                }
            } else if (filter.type === 'date') {
                valueInputHtml = `<input type="date" id="popup-val-input" class="form-control" style="height:32px;" value="${filter.value || ''}">`;
            } else if (filter.type === 'dropdown') {
                let optionsHtml = filter.options.map(o => `<option value="${o}" ${filter.value === o ? 'selected' : ''}>${o}</option>`).join('');
                valueInputHtml = `<select id="popup-val-input" class="form-control" style="height:32px; padding: 4px 8px;">${optionsHtml}</select>`;
            } else {
                valueInputHtml = `<input type="text" id="popup-val-input" class="form-control" style="height:32px;" value="${filter.value || ''}" placeholder="Nhập giá trị" maxlength="255">`;
            }

            popup.innerHTML = `
                <div style="font-weight:700; font-size:12px; color:var(--text-main); margin-bottom:2px;">Cấu hình: ${filter.label}</div>
                <div class="form-group">
                    <label class="form-label" style="font-size:10px;">Toán tử</label>
                    <select id="popup-operator-select" class="form-control" style="height:32px; padding: 4px 8px;" onchange="handlePopupOperatorChange(${idx})">
                        ${optHtml}
                    </select>
                </div>
                <div class="form-group" id="popup-val-container">
                    <label class="form-label" style="font-size:10px;">Giá trị</label>
                    ${valueInputHtml}
                    <span id="popup-val-error" style="color:#ef4444; font-size:10px; display:none; margin-top:2px;">Chưa chọn giá trị</span>
                </div>
                <div style="display:flex; justify-content:flex-end; gap:8px; margin-top:4px;">
                    <button class="btn btn-secondary" style="font-size:11px; padding:4px 10px; height:auto;" onclick="closeFilterConfigPopup()">Hủy</button>
                    <button class="btn btn-primary" style="font-size:11px; padding:4px 10px; height:auto;" onclick="applyFilterConfig(${idx})">Chọn</button>
                </div>
            `;

            document.body.appendChild(popup);
            activeConfigPopup = popup;

            // Stop click events from closing when clicking inside
            popup.onclick = (event) => event.stopPropagation();
        }

        function handlePopupOperatorChange(idx) {
            const select = document.getElementById('popup-operator-select');
            const container = document.getElementById('popup-val-container');
            if (!select || !container) return;

            const op = select.value;
            const filter = activeFilters[idx];

            let valueInputHtml = '';
            if (op === 'Có dữ liệu' || op === 'Không có dữ liệu') {
                valueInputHtml = `<label class="form-label" style="font-size:10px;">Giá trị</label>
                                 <input type="text" id="popup-val-input" class="form-control" style="height:32px;" disabled placeholder="Không cần nhập giá trị">`;
            } else if (op === 'Trong khoảng' || op === 'Ngoài khoảng') {
                if (filter.type === 'date') {
                    valueInputHtml = `<label class="form-label" style="font-size:10px;">Giá trị</label>
                                     <div style="display:flex; flex-direction:column; gap:6px;">
                                        <input type="date" id="popup-val-date1" class="form-control" style="height:32px;">
                                        <input type="date" id="popup-val-date2" class="form-control" style="height:32px;">
                                     </div>`;
                } else {
                    valueInputHtml = `<label class="form-label" style="font-size:10px;">Giá trị</label>
                                     <div style="display:flex; gap:6px;">
                                        <input type="number" id="popup-val-num1" class="form-control" style="height:32px; flex:1;" placeholder="Từ">
                                        <input type="number" id="popup-val-num2" class="form-control" style="height:32px; flex:1;" placeholder="Đến">
                                     </div>`;
                }
            } else if (filter.type === 'date') {
                valueInputHtml = `<label class="form-label" style="font-size:10px;">Giá trị</label>
                                 <input type="date" id="popup-val-input" class="form-control" style="height:32px;">`;
            } else if (filter.type === 'dropdown') {
                let optionsHtml = filter.options.map(o => `<option value="${o}">${o}</option>`).join('');
                valueInputHtml = `<label class="form-label" style="font-size:10px;">Giá trị</label>
                                 <select id="popup-val-input" class="form-control" style="height:32px; padding: 4px 8px;">${optionsHtml}</select>`;
            } else {
                valueInputHtml = `<label class="form-label" style="font-size:10px;">Giá trị</label>
                                 <input type="text" id="popup-val-input" class="form-control" style="height:32px;" placeholder="Nhập giá trị" maxlength="255">`;
            }

            container.innerHTML = valueInputHtml + `<span id="popup-val-error" style="color:#ef4444; font-size:10px; display:none; margin-top:2px;">Chưa chọn giá trị</span>`;
        }

        function applyFilterConfig(idx) {
            const filter = activeFilters[idx];
            const opSelect = document.getElementById('popup-operator-select');
            const errSpan = document.getElementById('popup-val-error');
            if (!opSelect) return;

            const operator = opSelect.value;
            let value = '';

            if (operator === 'Có dữ liệu' || operator === 'Không có dữ liệu') {
                value = '';
            } else if (operator === 'Trong khoảng' || operator === 'Ngoài khoảng') {
                if (filter.type === 'date') {
                    const d1 = document.getElementById('popup-val-date1').value;
                    const d2 = document.getElementById('popup-val-date2').value;
                    if (!d1 || !d2) {
                        if (errSpan) errSpan.style.display = 'block';
                        return;
                    }
                    value = `${d1}~${d2}`;
                } else {
                    const v1 = document.getElementById('popup-val-num1').value.trim();
                    const v2 = document.getElementById('popup-val-num2').value.trim();
                    if (!v1 || !v2) {
                        if (errSpan) errSpan.style.display = 'block';
                        return;
                    }
                    value = `${v1}~${v2}`;
                }
            } else {
                const inputEl = document.getElementById('popup-val-input');
                if (inputEl) {
                    value = inputEl.value.trim();
                    if (!value && filter.type !== 'dropdown') {
                        if (errSpan) errSpan.style.display = 'block';
                        return;
                    }
                }
            }

            if (errSpan) errSpan.style.display = 'none';

            // Apply to activeFilters
            filter.operator = operator;
            filter.value = value;

            closeFilterConfigPopup();
            renderContactsTable();
            showToast(`Áp dụng bộ lọc: ${filter.label} ${operator} "${value}"`);
        }

        function closeFilterConfigPopup() {
            const popup = document.getElementById('filter-config-popup');
            if (popup) {
                popup.remove();
            }
            activeConfigPopup = null;
        }

        // Close dropdown when clicking out
        window.addEventListener('click', (e) => {
            const advFilterBtn = document.getElementById('adv-filter-btn');
            const advFilterDropdown = document.getElementById('adv-filter-dropdown');
            if (advFilterDropdown && advFilterDropdown.style.display === 'block' && !advFilterBtn.contains(e.target) && !advFilterDropdown.contains(e.target)) {
                advFilterDropdown.style.display = 'none';
                const arrow = document.getElementById('adv-filter-arrow');
                if (arrow) arrow.style.transform = '';
            }

            // Close configuration popup if clicking out of it and not clicking tag status
            if (activeConfigPopup && !activeConfigPopup.contains(e.target) && !e.target.classList.contains('filter-tag-status')) {
                closeFilterConfigPopup();
            }
        });

        // CONTACT FORM MODAL (Tạo mới & Cập nhật)
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
        }

        // CONTACT DELETE MODAL (Xóa liên hệ)
        function openContactDeleteModal(contactId) {
            const modal = document.getElementById('contact-delete-modal');
            document.getElementById('contact-delete-id').value = contactId;
            modal.classList.add('open');
        }

        function closeContactDeleteModal() {
            document.getElementById('contact-delete-modal').classList.remove('open');
        }

        function confirmDeleteContact() {
            const id = document.getElementById('contact-delete-id').value;
            const c = contactsState.find(item => item.id === id);
            
            if (c) {
                // Business rule (SRS VI): "Trường hợp liên hệ đã phát sinh dữ liệu khác trong hệ thống, hiển thị thông báo: Khách hàng đã có đơn hàng, bạn không thể xóa."
                if (c.hasOrders) {
                    showToast("Khách hàng đã có đơn hàng, bạn không thể xóa.");
                    closeContactDeleteModal();
                    return;
                }

                contactsState = contactsState.filter(item => item.id !== id);
                showToast("Xóa liên hệ thành công");
            }
            closeContactDeleteModal();
            renderContactsTable();
        }

        // CONTACT EXPORT MODAL (Xuất file excel)
        function openContactExportModal() {
            document.getElementById('contact-export-modal').classList.add('open');
            toggleExportScopeWarning(false);
        }

        function closeContactExportModal() {
            document.getElementById('contact-export-modal').classList.remove('open');
        }

        function toggleExportScopeWarning(show) {
            const warning = document.getElementById('export-scope-warning');
            if (warning) {
                warning.style.display = show ? 'block' : 'none';
            }
        }

        function submitContactExport() {
            const scope = document.querySelector('input[name="export-scope"]:checked').value;
            closeContactExportModal();
            
            showToast("File Excel dữ liệu đang được xử lý! Bạn có thể tải file dữ liệu tại Cài đặt -> Quản lý xuất dữ liệu (AC6)");
            
            // Simulate background processing success after 3 seconds
            setTimeout(() => {
                showToast("Ai đó đã tải thành công file Excel danh sách khách hàng (AC7)");
            }, 3000);
        }

        // SSO MOCK DETAIL DISPLAY PAGE (Đăng nhập một lần - SSO)
        function openSsoProfile(contactId) {
            const c = contactsState.find(item => item.id === contactId);
            if (!c) return;

            const modal = document.getElementById('sso-profile-modal');
            const body = document.getElementById('sso-profile-body');

            const fullName = (c.lastName || '') + ' ' + (c.firstName || '');
            
            body.innerHTML = `
                <div style="background-color: var(--primary-light); border:1px solid var(--primary-border); padding:16px; border-radius:8px; margin-bottom: 20px;">
                    <h4 style="color: var(--primary-color); margin-bottom: 4px; font-weight:700;">Xác thực phiên kết nối thành công (SSO Active)</h4>
                    <p style="font-size:12px; color:var(--text-muted);">Hệ thống đã mã hóa Token ngắn hạn và liên kết an toàn từ cổng GapOne Conversation sang GapOne Portal Core (AC3, AC11)</p>
                </div>
                
                <div style="display:flex; gap:24px; align-items:flex-start; flex-wrap:wrap;">
                    <div style="width:120px; height:120px; border-radius:50%; background-color:#e2e8f0; display:flex; align-items:center; justify-content:center; font-size:48px; font-weight:700; color:#475569; border: 4px solid var(--border-color);">
                        ${c.firstName ? c.firstName[0] : 'C'}
                    </div>
                    <div style="flex:1; min-width:280px; display:flex; flex-direction:column; gap:12px;">
                        <h2 style="font-size:24px; font-weight:700; color:var(--text-main);">${fullName}</h2>
                        <p style="font-size:14px; color:var(--text-muted); margin-bottom:12px;">Mã khách hàng: <strong>${c.id}</strong></p>
                        
                        <div style="display:grid; grid-template-columns: 140px 1fr; gap:10px 20px; font-size:14px; border-top:1px solid var(--border-color); padding-top:16px;">
                            <div style="font-weight:600; color:var(--text-muted);">Số điện thoại:</div>
                            <div style="color:var(--text-main); font-weight:700;">${c.phone || '−'}</div>

                            <div style="font-weight:600; color:var(--text-muted);">Email:</div>
                            <div style="color:var(--text-main);">${c.email || '−'}</div>

                            <div style="font-weight:600; color:var(--text-muted);">Ngày sinh:</div>
                            <div style="color:var(--text-main);">${c.dob ? c.dob.split('-').reverse().join('/') : '−'}</div>

                            <div style="font-weight:600; color:var(--text-muted);">Địa chỉ:</div>
                            <div style="color:var(--text-main);">${c.address || '−'}</div>

                            <div style="font-weight:600; color:var(--text-muted);">Địa chỉ tạm trú:</div>
                            <div style="color:var(--text-main);">${c.addressTemp || '−'}</div>

                            <div style="font-weight:600; color:var(--text-muted);">Công ty:</div>
                            <div style="color:var(--text-main);">${c.company || '−'}</div>

                            <div style="font-weight:600; color:var(--text-muted);">Chức vụ/Vị trí:</div>
                            <div style="color:var(--text-main);">${c.position || '−'}</div>

                            <div style="font-weight:600; color:var(--text-muted);">Nhân viên phụ trách:</div>
                            <div style="color:var(--text-main); font-weight:600; color:var(--primary-color);">${c.assignee}</div>
                        </div>
                    </div>
                </div>
            `;

            modal.classList.add('open');
            showToast(`SSO: Đăng nhập một lần mở Profile của "${fullName}" (AC2)`);
        }

        function closeSsoProfileModal() {
            document.getElementById('sso-profile-modal').classList.remove('open');
        }
"""

html = html.replace(js_target, contacts_js_logic + js_target)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Modification Completed Successfully!")
