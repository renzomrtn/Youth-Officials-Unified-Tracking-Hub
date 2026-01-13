# models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Tenant(Base):
    __tablename__ = "tenants"
    
    tenant_id = Column(Integer, primary_key=True, index=True)
    tenant_name = Column(String, index=True)
    is_federation = Column (Boolean, default=False)
    tenant_status = Column(String)
    

class Position(Base):
    __tablename__ = "positions"
    
    position_id = Column(Integer, primary_key=True, index=True)
    position_name = Column(String, index=True)
    is_barangay_sk_role = Column(Boolean, default=False)
    is_federation_role = Column(Boolean, default=True)


class Account(Base):
    __tablename__ = "accounts"
    
    account_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    contact_number = Column(String)
    contact_email = Column(String)
    account_status = Column(String)
    

class AccountTenantRole(Base):
    __tablename__ = "account_tenant_roles"
    
    role_id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.account_id"))
    tenant_id = Column(Integer, ForeignKey("tenants.tenant_id"))
    position_id = Column(Integer, ForeignKey("positions.position_id"))
    is_primary_tenant = Column(Boolean, default=False)
    role_status = Column(String)
    
    account = relationship("Account")
    tenant = relationship("Tenant")
    position = relationship("Position")


class Personnel(Base):
    __tablename__ = "personnel"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String, index=True)


class NeedsCategory(Base):
    __tablename__ = "needs_categories"
    
    category_id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.tenant_id"))
    category_name = Column(String, index=True)
    scope = Column(String)

    tenant = relationship("Tenant")


class DocumentCategory(Base):
    doc_category_id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.tenant_id"))
    category_name = Column(String, index=True)

    tenant = relationship("Tenant")


class Archive(Base):
    __tablename__ = "archive"
    
    archive_id = Column(String, primary_key=True, index=True)
    recode_code = Column(String)
    tenant_id = Column(Integer, ForeignKey("tenants.tenant_id"))
    doc_category_id = Column(Integer, ForeignKey("document.category_id"))
    last_editor = Column(String)
    title = Column(String)
    file_name = Column(String)
    file_path = Column(String)
    file_size = Column(Float)
    uploaded_at = Column(DateTime)
    updated_at = Column(DateTime)

    tenant = relationship("Tenant")
    document_category = relationship("DocumentCategory")


class Author(Base):
    __tablename__ = "authors"

    doc_author_id = Column(Integer, primary_key=True, index=True)
    archive_id = Column(String, ForeignKey("archive.archive_id"))
    role_id = Column(Integer, ForeignKey("positions.position_id"))

    archive = relationship("Archive")
    position = relationship("Position")


class NeedsAssessment(Base):
    __tablename__ = "needs_assessment_records"
    
    needs_id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.tenant_id"))
    category_id = Column(Integer, ForeignKey("needs_categories.category_id"))
    archive_id = Column(String, ForeignKey("archive.id"))
    description = Column(String)
    proposed_solution = Column(String)
    year_identified = Column(Date)
    status = Column(String)

    tenant = relationship("Tenant")
    category = relationship("NeedsCategory")
    archive = relationship("Archive")


class Budget(Base):
    __tablename__ = "budgets"
    
    budget_id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.tenant_id"))
    archive_id = Column(String, ForeignKey("archive.id"))
    fiscal_year = Column(Date)
    budget_type = Column(String)
    total_amount = Column(Float)

    tenant = relationship("Tenant")
    archive = relationship("Archive")


class LineItem(Base):
    __tablename__ = "line_items"
    
    line_item_id = Column(Integer, primary_key=True, index=True)
    budget_id = Column(Integer, ForeignKey("budgets.budget_id"))
    tenant_id = Column(Integer, ForeignKey("tenants.tenant_id"))
    needs_id = Column(Integer, ForeignKey("needs_assessment_records.needs_id"))
    line_item_name = Column(String)
    activity_type = Column(String)
    justification = Column(String)
    amount_allocated = Column(Float)
    amount_remaining = Column(Float)
    period_start = Column(Date)
    period_end = Column(Date)
    status = Column(String)

    budget = relationship("Budget")


class Augmentation(Base):
    __tablename__ = "augmentations"
    
    augmentation_id = Column(Integer, primary_key=True, index=True)
    line_item_id = Column(Integer, ForeignKey("line_items.line_item_id"))
    archive_id = Column(String, ForeignKey("archive.id"))
    org_name = Column(String)

    line_item = relationship("LineItem")
    archive = relationship("Archive")


class AugmentationDetail(Base):
    __tablename__ = "augmentation_details"
    
    detail_id = Column(Integer, primary_key=True, index=True)
    augmentation_id = Column(Integer, ForeignKey("augmentations.augmentation_id"))
    resource_type = Column(String)
    item_name = Column(String)
    amount_value = Column(Float)
    service_description = Column(String)

    augmentation = relationship("Augmentation")


class Project(Base):
    __tablename__ = "projects"
    
    project_id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.tenant_id"))
    line_item_id = Column(Integer, ForeignKey("line_items.line_item_id"))
    proponent = Column(String)
    project_title = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    project_status = Column(String)
    expense_verif_status = Column(String)

    line_item = relationship("LineItem")


class CommitteeCategory(Base):
    __tablename__ = "committee_categories"
    
    committee_cat_id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.tenant_id"))
    category_name = Column(String, index=True)

    tenant = relationship("Tenant")


class ProjectCommittee(Base):
    __tablename__ = "project_committees"
    
    committee_id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.project_id"))
    committee_cat_id = Column(Integer, ForeignKey("committee_categories.committee_cat_id"))

    project = relationship("Project")
    committee_category = relationship("CommitteeCategory")


class ProjectTask(Base):
    __tablename__ = "project_tasks"
    
    task_id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.project_id"))
    task_name = Column(String)
    due_date = Column(Date)
    task_status = Column(String)
    priority_level = Column(String)

    project = relationship("Project")


class ProjectTaskAssignment(Base):
    __tablename__ = "project_task_assignments"
    
    assignment_id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("project_tasks.task_id"))
    personnel_id = Column(Integer, ForeignKey("personnel.id"))

    task = relationship("ProjectTask")
    personnel = relationship("Personnel")


class Expenditure(Base):
    __tablename__ = "expenditures"
    
    expenditure_id = Column(Integer, primary_key=True, index=True)
    line_item_id = Column(Integer, ForeignKey("line_items.line_item_id"))
    personnel_id = Column(Integer, ForeignKey("personnel.id"))
    status = Column(String)
    total_amount_spent = Column(Float)

    project = relationship("Project")
    archive = relationship("Archive")


class ExpenditureParticular(Base):
    __tablename__ = "expenditure_particulars"
    
    particular_id = Column(Integer, primary_key=True, index=True)
    expenditure_id = Column(Integer, ForeignKey("expenditures.expenditure_id"))
    particular_name = Column(String)
    amount_claimed = Column(Float)
    date_of_expense = Column(Date)
    attachment = Column(String)

    expenditure = relationship("Expenditure")


class VerificationFlagging(Base):
    __tablename__ = "verification_flaggings"
    
    verification_id = Column(Integer, primary_key=True, index=True)
    particular_id = Column(Integer, ForeignKey("expenditure_particulars.particular_id"))
    personnel_id = Column(Integer, ForeignKey("personnel.id"))
    flag_particular = Column(String)
    flag_amount = Column(Float)
    flag_date = Column(Date)
    flag_attachments = Column(String)
    remarks = Column(String)
    created_at = Column(DateTime)

    particular_id = relationship("ExpenditureParticular")
    personnel = relationship("Personnel")


class Correction(Base):
    __tablename__ = "corrections"
    
    correction_id = Column(Integer, primary_key=True, index=True)
    verification_id = Column(Integer, ForeignKey("verification_flaggings.verification_id"))
    particular_id = Column(Integer, ForeignKey("expenditure_particulars.particular_id"))
    field_name = Column(String)
    old_value = Column(Float)
    new_value = Column(Float)
    explanation = Column(String)

    verification_flagging = relationship("VerificationFlagging")
    particular = relationship("ExpenditureParticular")


class CMS(Base):
    __tablename__ = "cms_contents"
    
    portal_item_id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.tenant_id"))
    archive_id = Column(String, ForeignKey("archive.id"))
    line_item_id = Column(String, ForeignKey("line_items.line_item_id"))
    expenditure_id = Column(String, ForeignKey("expenditures.expenditure_id"))
    is_published = Column(Boolean, default=False)
    status = Column(String)

    tenant = relationship("Tenant")