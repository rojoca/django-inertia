(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-9d5345d2"],{"0f53":function(t,e,r){"use strict";var n=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[t.label?r("label",{staticClass:"form-label",attrs:{for:t.id}},[t._v(t._s(t.label)+":")]):t._e(),r("input",t._b({ref:"input",staticClass:"form-input",class:{error:t.errors.length},attrs:{id:t.id,type:t.type},domProps:{value:t.value},on:{input:function(e){return t.$emit("input",e.target.value)}}},"input",t.$attrs,!1)),t.errors.length?r("div",{staticClass:"form-error"},[t._v(t._s(t.errors[0]))]):t._e()])},a=[],s={inheritAttrs:!1,props:{id:{type:String,default:function(){return"text-input-".concat(this._uid)}},type:{type:String,default:"text"},value:String,label:String,errors:{type:Array,default:function(){return[]}}},methods:{focus:function(){this.$refs.input.focus()},select:function(){this.$refs.input.select()},setSelectionRange:function(t,e){this.$refs.input.setSelectionRange(t,e)}}},o=s,i=r("2877"),l=Object(i["a"])(o,n,a,!1,null,null,null);e["a"]=l.exports},1148:function(t,e,r){"use strict";var n=r("a691"),a=r("1d80");t.exports="".repeat||function(t){var e=String(a(this)),r="",s=n(t);if(s<0||s==1/0)throw RangeError("Wrong number of repetitions");for(;s>0;(s>>>=1)&&(e+=e))1&s&&(r+=e);return r}},"1be4":function(t,e,r){var n=r("d066");t.exports=n("document","documentElement")},"37e8":function(t,e,r){var n=r("83ab"),a=r("9bf2"),s=r("825a"),o=r("df75");t.exports=n?Object.defineProperties:function(t,e){s(t);var r,n=o(e),i=n.length,l=0;while(i>l)a.f(t,r=n[l++],e[r]);return t}},"3bbe":function(t,e,r){var n=r("861d");t.exports=function(t){if(!n(t)&&null!==t)throw TypeError("Can't set "+String(t)+" as a prototype");return t}},"3f0d":function(t,e,r){"use strict";var n=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("button",{staticClass:"flex items-center",attrs:{disabled:t.loading}},[t.loading?r("div",{staticClass:"btn-spinner mr-2"}):t._e(),t._t("default")],2)},a=[],s={props:{loading:Boolean}},o=s,i=r("2877"),l=Object(i["a"])(o,n,a,!1,null,null,null);e["a"]=l.exports},"408a":function(t,e,r){var n=r("c6b6");t.exports=function(t){if("number"!=typeof t&&"Number"!=n(t))throw TypeError("Incorrect invocation");return+t}},5899:function(t,e){t.exports="\t\n\v\f\r                　\u2028\u2029\ufeff"},"58a8":function(t,e,r){var n=r("1d80"),a=r("5899"),s="["+a+"]",o=RegExp("^"+s+s+"*"),i=RegExp(s+s+"*$"),l=function(t){return function(e){var r=String(n(e));return 1&t&&(r=r.replace(o,"")),2&t&&(r=r.replace(i,"")),r}};t.exports={start:l(1),end:l(2),trim:l(3)}},"61ae":function(t,e,r){"use strict";var n=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[t.label?r("label",{staticClass:"form-label"},[t._v(t._s(t.label)+":")]):t._e(),r("div",{staticClass:"form-input p-0",class:{error:t.errors.length}},[r("input",{ref:"file",staticClass:"hidden",attrs:{type:"file",accept:t.accept},on:{change:t.change}}),t.value?r("div",{staticClass:"flex items-center justify-between p-2"},[r("div",{staticClass:"flex-1 pr-1"},[t._v(t._s(t.value.name)+" "),r("span",{staticClass:"text-gray-500 text-xs"},[t._v("("+t._s(t.filesize(t.value.size))+")")])]),r("button",{staticClass:"px-4 py-1 bg-gray-500 hover:bg-gray-700 rounded-sm text-xs font-medium text-white",attrs:{type:"button"},on:{click:t.remove}},[t._v(" Remove ")])]):r("div",{staticClass:"p-2"},[r("button",{staticClass:"px-4 py-1 bg-gray-500 hover:bg-gray-700 rounded-sm text-xs font-medium text-white",attrs:{type:"button"},on:{click:t.browse}},[t._v(" Browse ")])])]),t.errors.length?r("div",{staticClass:"form-error"},[t._v(t._s(t.errors[0]))]):t._e()])},a=[],s=(r("b680"),{props:{value:File,label:String,accept:String,errors:{type:Array,default:function(){return[]}}},watch:{value:function(t){t||(this.$refs.file.value="")}},methods:{filesize:function(t){var e=Math.floor(Math.log(t)/Math.log(1024));return 1*(t/Math.pow(1024,e)).toFixed(2)+" "+["B","kB","MB","GB","TB"][e]},browse:function(){this.$refs.file.click()},change:function(t){this.$emit("input",t.target.files[0])},remove:function(){this.$emit("input",null)}}}),o=s,i=r("2877"),l=Object(i["a"])(o,n,a,!1,null,null,null);e["a"]=l.exports},"64a7":function(t,e,r){"use strict";r.r(e);var n=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("h1",{staticClass:"mb-8 font-bold text-3xl"},[r("inertia-link",{staticClass:"text-indigo-400 hover:text-indigo-600",attrs:{href:t.route("users")}},[t._v("Users")]),r("span",{staticClass:"text-indigo-400 font-medium"},[t._v("/")]),t._v(" Create ")],1),r("div",{staticClass:"bg-white rounded shadow overflow-hidden max-w-3xl"},[r("form",{on:{submit:function(e){return e.preventDefault(),t.submit(e)}}},[r("div",{staticClass:"p-8 -mr-6 -mb-8 flex flex-wrap"},[r("text-input",{staticClass:"pr-6 pb-8 w-full lg:w-1/2",attrs:{errors:t.$page.errors.first_name,label:"First name"},model:{value:t.form.first_name,callback:function(e){t.$set(t.form,"first_name",e)},expression:"form.first_name"}}),r("text-input",{staticClass:"pr-6 pb-8 w-full lg:w-1/2",attrs:{errors:t.$page.errors.last_name,label:"Last name"},model:{value:t.form.last_name,callback:function(e){t.$set(t.form,"last_name",e)},expression:"form.last_name"}}),r("text-input",{staticClass:"pr-6 pb-8 w-full lg:w-1/2",attrs:{errors:t.$page.errors.email,label:"Email"},model:{value:t.form.email,callback:function(e){t.$set(t.form,"email",e)},expression:"form.email"}}),r("text-input",{staticClass:"pr-6 pb-8 w-full lg:w-1/2",attrs:{errors:t.$page.errors.password,type:"password",autocomplete:"new-password",label:"Password"},model:{value:t.form.password,callback:function(e){t.$set(t.form,"password",e)},expression:"form.password"}}),r("select-input",{staticClass:"pr-6 pb-8 w-full lg:w-1/2",attrs:{errors:t.$page.errors.owner,label:"Owner"},model:{value:t.form.owner,callback:function(e){t.$set(t.form,"owner",e)},expression:"form.owner"}},[r("option",{domProps:{value:!0}},[t._v("Yes")]),r("option",{domProps:{value:!1}},[t._v("No")])]),r("file-input",{staticClass:"pr-6 pb-8 w-full lg:w-1/2",attrs:{errors:t.$page.errors.photo,type:"file",accept:"image/*",label:"Photo"},model:{value:t.form.photo,callback:function(e){t.$set(t.form,"photo",e)},expression:"form.photo"}})],1),r("div",{staticClass:"px-8 py-4 bg-gray-100 border-t border-gray-200 flex justify-end items-center"},[r("loading-button",{staticClass:"btn-indigo",attrs:{loading:t.sending,type:"submit"}},[t._v("Create User")])],1)])])])},a=[],s=r("ba40"),o=r("3f0d"),i=r("e8a6"),l=r("0f53"),u=r("61ae"),c={metaInfo:{title:"Create User"},layout:s["a"],components:{LoadingButton:o["a"],SelectInput:i["a"],TextInput:l["a"],FileInput:u["a"]},remember:"form",data:function(){return{sending:!1,form:{first_name:null,last_name:null,email:null,password:null,owner:!1,photo:null}}},methods:{submit:function(){var t=this;this.sending=!0;var e=new FormData;e.append("first_name",this.form.first_name||""),e.append("last_name",this.form.last_name||""),e.append("email",this.form.email||""),e.append("password",this.form.password||""),e.append("owner",this.form.owner?"1":"0"),e.append("photo",this.form.photo||""),this.$inertia.post(this.route("users.store"),e).then((function(){return t.sending=!1}))}}},f=c,p=r("2877"),d=Object(p["a"])(f,n,a,!1,null,null,null);e["default"]=d.exports},7156:function(t,e,r){var n=r("861d"),a=r("d2bb");t.exports=function(t,e,r){var s,o;return a&&"function"==typeof(s=e.constructor)&&s!==r&&n(o=s.prototype)&&o!==r.prototype&&a(t,o),t}},"7c73":function(t,e,r){var n,a=r("825a"),s=r("37e8"),o=r("7839"),i=r("d012"),l=r("1be4"),u=r("cc12"),c=r("f772"),f=">",p="<",d="prototype",m="script",v=c("IE_PROTO"),b=function(){},h=function(t){return p+m+f+t+p+"/"+m+f},g=function(t){t.write(h("")),t.close();var e=t.parentWindow.Object;return t=null,e},_=function(){var t,e=u("iframe"),r="java"+m+":";return e.style.display="none",l.appendChild(e),e.src=String(r),t=e.contentWindow.document,t.open(),t.write(h("document.F=Object")),t.close(),t.F},w=function(){try{n=document.domain&&new ActiveXObject("htmlfile")}catch(e){}w=n?g(n):_();var t=o.length;while(t--)delete w[d][o[t]];return w()};i[v]=!0,t.exports=Object.create||function(t,e){var r;return null!==t?(b[d]=a(t),r=new b,b[d]=null,r[v]=t):r=w(),void 0===e?r:s(r,e)}},a9e3:function(t,e,r){"use strict";var n=r("83ab"),a=r("da84"),s=r("94ca"),o=r("6eeb"),i=r("5135"),l=r("c6b6"),u=r("7156"),c=r("c04e"),f=r("d039"),p=r("7c73"),d=r("241c").f,m=r("06cf").f,v=r("9bf2").f,b=r("58a8").trim,h="Number",g=a[h],_=g.prototype,w=l(p(_))==h,x=function(t){var e,r,n,a,s,o,i,l,u=c(t,!1);if("string"==typeof u&&u.length>2)if(u=b(u),e=u.charCodeAt(0),43===e||45===e){if(r=u.charCodeAt(2),88===r||120===r)return NaN}else if(48===e){switch(u.charCodeAt(1)){case 66:case 98:n=2,a=49;break;case 79:case 111:n=8,a=55;break;default:return+u}for(s=u.slice(2),o=s.length,i=0;i<o;i++)if(l=s.charCodeAt(i),l<48||l>a)return NaN;return parseInt(s,n)}return+u};if(s(h,!g(" 0o1")||!g("0b1")||g("+0x1"))){for(var y,C=function(t){var e=arguments.length<1?0:t,r=this;return r instanceof C&&(w?f((function(){_.valueOf.call(r)})):l(r)!=h)?u(new g(x(e)),r,C):x(e)},$=n?d(g):"MAX_VALUE,MIN_VALUE,NaN,NEGATIVE_INFINITY,POSITIVE_INFINITY,EPSILON,isFinite,isInteger,isNaN,isSafeInteger,MAX_SAFE_INTEGER,MIN_SAFE_INTEGER,parseFloat,parseInt,isInteger".split(","),E=0;$.length>E;E++)i(g,y=$[E])&&!i(C,y)&&v(C,y,m(g,y));C.prototype=_,_.constructor=C,o(a,h,C)}},b680:function(t,e,r){"use strict";var n=r("23e7"),a=r("a691"),s=r("408a"),o=r("1148"),i=r("d039"),l=1..toFixed,u=Math.floor,c=function(t,e,r){return 0===e?r:e%2===1?c(t,e-1,r*t):c(t*t,e/2,r)},f=function(t){var e=0,r=t;while(r>=4096)e+=12,r/=4096;while(r>=2)e+=1,r/=2;return e},p=l&&("0.000"!==8e-5.toFixed(3)||"1"!==.9.toFixed(0)||"1.25"!==1.255.toFixed(2)||"1000000000000000128"!==(0xde0b6b3a7640080).toFixed(0))||!i((function(){l.call({})}));n({target:"Number",proto:!0,forced:p},{toFixed:function(t){var e,r,n,i,l=s(this),p=a(t),d=[0,0,0,0,0,0],m="",v="0",b=function(t,e){var r=-1,n=e;while(++r<6)n+=t*d[r],d[r]=n%1e7,n=u(n/1e7)},h=function(t){var e=6,r=0;while(--e>=0)r+=d[e],d[e]=u(r/t),r=r%t*1e7},g=function(){var t=6,e="";while(--t>=0)if(""!==e||0===t||0!==d[t]){var r=String(d[t]);e=""===e?r:e+o.call("0",7-r.length)+r}return e};if(p<0||p>20)throw RangeError("Incorrect fraction digits");if(l!=l)return"NaN";if(l<=-1e21||l>=1e21)return String(l);if(l<0&&(m="-",l=-l),l>1e-21)if(e=f(l*c(2,69,1))-69,r=e<0?l*c(2,-e,1):l/c(2,e,1),r*=4503599627370496,e=52-e,e>0){b(0,r),n=p;while(n>=7)b(1e7,0),n-=7;b(c(10,n,1),0),n=e-1;while(n>=23)h(1<<23),n-=23;h(1<<n),b(1,1),h(2),v=g()}else b(0,r),b(1<<-e,0),v=g()+o.call("0",p);return p>0?(i=v.length,v=m+(i<=p?"0."+o.call("0",p-i)+v:v.slice(0,i-p)+"."+v.slice(i-p))):v=m+v,v}})},d2bb:function(t,e,r){var n=r("825a"),a=r("3bbe");t.exports=Object.setPrototypeOf||("__proto__"in{}?function(){var t,e=!1,r={};try{t=Object.getOwnPropertyDescriptor(Object.prototype,"__proto__").set,t.call(r,[]),e=r instanceof Array}catch(s){}return function(r,s){return n(r),a(s),e?t.call(r,s):r.__proto__=s,r}}():void 0)},df75:function(t,e,r){var n=r("ca84"),a=r("7839");t.exports=Object.keys||function(t){return n(t,a)}},e8a6:function(t,e,r){"use strict";var n=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[t.label?r("label",{staticClass:"form-label",attrs:{for:t.id}},[t._v(t._s(t.label)+":")]):t._e(),r("select",t._b({directives:[{name:"model",rawName:"v-model",value:t.selected,expression:"selected"}],ref:"input",staticClass:"form-select",class:{error:t.errors.length},attrs:{id:t.id},on:{change:function(e){var r=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.selected=e.target.multiple?r:r[0]}}},"select",t.$attrs,!1),[t._t("default")],2),t.errors.length?r("div",{staticClass:"form-error"},[t._v(t._s(t.errors[0]))]):t._e()])},a=[],s=(r("a9e3"),{inheritAttrs:!1,props:{id:{type:String,default:function(){return"select-input-".concat(this._uid)}},value:[String,Number,Boolean],label:String,errors:{type:Array,default:function(){return[]}}},data:function(){return{selected:this.value}},watch:{selected:function(t){this.$emit("input",t)}},methods:{focus:function(){this.$refs.input.focus()},select:function(){this.$refs.input.select()}}}),o=s,i=r("2877"),l=Object(i["a"])(o,n,a,!1,null,null,null);e["a"]=l.exports}}]);
//# sourceMappingURL=chunk-9d5345d2.js.map?id=15c559fb84224f875286