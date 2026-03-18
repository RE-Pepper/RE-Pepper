

# File alExecuteDirector.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Execute**](dir_a22e87c788a1f2e7d5d5429c64840582.md) **>** [**alExecuteDirector.h**](al_execute_director_8h.md)

[Go to the documentation of this file](al_execute_director_8h.md)


```C++
#pragma once

#include <Functor/alFunctorBase.h>

namespace al
{

class ExecuteRequestKeeper;
class ExecuteTableHolderDraw;
class ExecuteTableHolderUpdate;

class IUseExecutor
{
public:
        virtual void execute()
        {
        }

        virtual void draw()
        {
        }
};

class ExecuteDirector
{
        friend class LayoutKit;

private:
        size_t                    _0;
        ExecuteTableHolderUpdate* mUpdateTable;
        int                       mDrawTableAmount;
        ExecuteTableHolderDraw**  mDrawTables;
        ExecuteRequestKeeper*     mRequestKeeper;
        void*                     _14;
        void*                     _18;

public:
        void init();
        void createExecutorListTable();
        void registerUser( al::IUseExecutor* p, const char* str );
        void registerFunctor( const al::FunctorBase& base, const char* str );
        void registerFunctorDraw( const al::FunctorBase& base, const char* str );

public:
        ExecuteDirector( int );
};

} // namespace al
```


