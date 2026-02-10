$$$

RO_SECTION §O
{
    RO +0
    {
        * (+CONST)
    }
    STATIC_INIT  +0 
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
    RW +0
    {
        * (+RW-DATA)
    }
    ZI +0
    {
        * (+ZI)
    }
}

MODULE_INFO     (0x00100000 + (0x04000000 - 0x00100000))
{
    .module_id  (0x00100000 + (0x04000000 - 0x00100000))
    {
        * (.module_id)
    }
}

GARBAGE_SECTION §R
{
    REST_SECTION §R
    {
        * (+CODE)
    }
}
