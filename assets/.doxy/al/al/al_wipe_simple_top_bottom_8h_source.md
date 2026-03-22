

# File alWipeSimpleTopBottom.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Layout**](dir_df428175ad75013516ece83f85ae05d3.md) **>** [**alWipeSimpleTopBottom.h**](al_wipe_simple_top_bottom_8h.md)

[Go to the documentation of this file](al_wipe_simple_top_bottom_8h.md)


```C++
#pragma once

namespace al
{

class WipeSimple;

class WipeSimpleTopBottom
{
private:
        WipeSimple* mTop;
        WipeSimple* mBottom;

public:
        inline WipeSimple* getTop() const
        {
                return mTop;
        }

        inline WipeSimple* getBottom() const
        {
                return mBottom;
        }

        bool isCloseEnd() const;

public:
        WipeSimpleTopBottom( const char* name, const char* archive, const char*, const LayoutInitInfo& info, const char* subArchive );
};

} // namespace al
```


