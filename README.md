# NCYU_API  

## Usage  
### GET `/course/{id}`  
### GET `/course/general`  
### GET `/course/department`
* Response
    * id
    * select-type（選擇類別）
    * class-type（課程類別）
    * class-name（課程名稱）
    * department（開課系所）
    * system（學制）
    * academy（學院）
    * grade（上課年級）
    * course-type（必選修）
    * scores（學分數）
    * remark（備註）
    * teacher（教師名稱）
    * week（上課星期）
    * session（上課節次）
    * classroom（教室）
    * campus（校區）

### GET `/deparments` 取得所有系所
* Response
    * `id(string)` : 系所標號
    * `content(string array)`
        * 學院
        * 學制
        * 學系

### GET `/department/{id}` 取得系所  
* Response
    * `id(string)` : 系所標號
    * `content(string array)`
        * 學院
        * 學制
        * 學系
