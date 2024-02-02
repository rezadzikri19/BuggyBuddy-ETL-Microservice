class RawBugReport:
  def __init__(self,
               bug_id: int,
               report_type: str,
               status: str,
               product: str,
               component: str,
               platform: str,
               summary: str,
               description: str,
               resolution: str,
               severity: str,
               duplicates):
    self.bug_id = bug_id,
    self.report_type = report_type,
    self.status = status,
    self.product = product,
    self.component = component,
    self.platform = platform,
    self.summary = summary,
    self.description = description,
    self.resolution = resolution,
    self.severity = severity,
    self.duplicates = duplicates,
    
  def __str__(self) -> str:
    return f"RawBugReport(bug_id={self.bug_id}, report_type={self.report_type}, summary={self.summary})"