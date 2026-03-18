

# File alByamlData.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Yaml**](dir_ead735227c22214cb122acbd07613fdc.md) **>** [**alByamlData.h**](al_byaml_data_8h.md)

[Go to the documentation of this file](al_byaml_data_8h.md)


```C++
#pragma once

namespace al
{

enum ByamlDataType
{
        ByamlDataType_Invalid     = 0,
        ByamlDataType_String      = 0xA0,
        ByamlDataType_Binary      = 0xA1,
        ByamlDataType_Array       = 0xC0,
        ByamlDataType_Hash        = 0xC1,
        ByamlDataType_StringTable = 0xC2,
        ByamlDataType_Bool        = 0xD0,
        ByamlDataType_Int         = 0xD1,
        ByamlDataType_Float       = 0xD2,
        ByamlDataType_Null        = 0xFF
};

class ByamlData
{
private:
        union Value
        {
                int   vInt;
                float vFloat;
        } mValue;

        ByamlDataType mType;

public:
        ByamlDataType getType() const
        {
                return mType;
        }

        int getIntValue() const
        {
                return mValue.vInt;
        }

        float getFloatValue() const
        {
                return mValue.vFloat;
        }
};

} // namespace al
```


