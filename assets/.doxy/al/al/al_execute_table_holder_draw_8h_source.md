

# File alExecuteTableHolderDraw.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Execute**](dir_a22e87c788a1f2e7d5d5429c64840582.md) **>** [**alExecuteTableHolderDraw.h**](al_execute_table_holder_draw_8h.md)

[Go to the documentation of this file](al_execute_table_holder_draw_8h.md)


```C++
#pragma once

namespace al
{

class ExecuteOrder;
class FunctorBase;

class IUseExecutor;

class ExecuteTableHolderDraw
{
        friend class ExecuteDirector;

private:
        int   _0;
        int   _4;
        int   _8;
        int   _C;
        int   _10;
        int   _14;
        int   _18;
        int   _1C;
        int   _20;
        int   _24;
        int   _28;
        int   _2C;
        int   _30;
        int   _34;
        int   _38;
        int   _3C;
        int   _40;
        int   _44;
        void* _48;
        void* _4C;

public:
        void init( const char*, const ExecuteOrder* order, int );
        void createExecutorListTable();
        void tryRegisterUser( al::IUseExecutor* p, const char* name );
        void tryRegisterFunctor( const al::FunctorBase& base, const char* name );

public:
        ExecuteTableHolderDraw();
};

} // namespace al
```


