variable "bucket" {
    description = "Name of bucket"
    type = string
    default = null
}

variable "acl" {
    description = "Acces control policy"
    type = string
    default = private
}

variable "policy"{
    description = "A bucket policy"
    type = string
    default = null
}

variable "tags" {
    description = "Mapping of tags to assign in bucket"
    type = map(string)
    default = {}
}

variable "object" {
    description = "Provides an s3 object to a bucket"
    type = string
    default = null
}

variable "key" {
    description = "Object key"
    type = string
    default = private
}

variable "index_document" {
    description = "Example suffix file"
    type = string
    default = private
}   

variable "error_document" {
    description = "Example key file"
    type = string
    default = private
}

