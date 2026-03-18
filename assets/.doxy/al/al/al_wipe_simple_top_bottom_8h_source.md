

# File alWipeSimpleTopBottom.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Layout**](dir_71ac96d9eee999c5231127773bfe6eda.md) **>** [**alWipeSimpleTopBottom.h**](al_wipe_simple_top_bottom_8h.md)

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


