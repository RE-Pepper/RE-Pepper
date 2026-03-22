#pragma once

#include <Yaml/alByamlData.h>

namespace al
{

class ByamlContainerHeader
{
private:
        // ByamlDataType mType : 1;
        // u32 mSize : 3;
        union
        {
                u32 mSize;
                u8  mType;
        };

public:
        inline ByamlDataType getType() const
        {
                return (ByamlDataType)mType;
        }

        inline u32 getCount() const
        {
                return mSize >> 8;
        } // get last 3 bytes
};

} // namespace al
