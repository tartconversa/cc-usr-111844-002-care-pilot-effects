def household_history(rows, household):
    """按月返回家庭原始观测，地区字段保持来源记录。"""
    return sorted((dict(r) for r in rows if r['household']==household),key=lambda r:r['month'])

def residence_at(panel,moves,household,month):
    """按迁移记录查询当月居住地，未有迁移记录时保留报送地区。"""
    changes=[r for r in moves if r['household']==household and r['month'] <= month]
    if changes:
        return max(changes,key=lambda r:r['month'])['district']
    reports=[r for r in panel if r['household']==household and r['month'] <= month]
    return max(reports,key=lambda r:r['month'])['district'] if reports else None

def raw_district_means(panel):
    """核对报送地区原始照护小时均值，不解释政策效果。"""
    groups={}
    for row in panel:
        if row['care_hours'] is not None:
            groups.setdefault(row['district'],[]).append(row['care_hours'])
    return {k:sum(v)/len(v) for k,v in groups.items()}
