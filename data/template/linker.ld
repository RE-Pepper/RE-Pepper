TEXT_SECTION 0x00100000
{
$$$}

RO_SECTION §O
{
&&&    STATIC_INIT  +0 
    {
        * (.static_init)
    }
    ET +0
    {
        * (.ARM.exidx)
        * (.ARM.extab)
    }
}

RW_SECTION §W
{
###}

MODULE_INFO     (0x00100000 + (0x04000000 - 0x00100000))
{
    .module_id  (0x00100000 + (0x04000000 - 0x00100000))
    {
        * (.module_id)
    }
}

GARBAGE_SECTION +0
{
    REST_SECTION +0
    {
        * (+CODE)
    }
}
