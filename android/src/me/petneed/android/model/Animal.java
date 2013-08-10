package me.petneed.android.model;

/**
 * Created by Jacob Chen on 8/10/13.
 */
public class Animal {
    public Animal(String name, String type, String image_file) {
        this.name = name;
        this.type = type;
        this.image_file = image_file;
    }

    public Animal(){

    }
    //private int accept_num;

    public String getName() {
        return name;
    }

    public String getSex() {
        return sex;
    }

    public String getType() {
        return type;
    }

    public String getBuild() {
        return build;
    }

    public String getAge() {
        return age;
    }

    public String getVariety() {
        return variety;
    }

    public String getReason() {
        return reason;
    }

    public String getAccept_num() {
        return accept_num;
    }

    public long getAcceptNumValue() {
        try{
        return Long.parseLong(accept_num);
        }
        catch (NumberFormatException nfe){
            return 0;
        }
    }
    public String getChip_num() {
        return chip_num;
    }

    public String getIs_sterilization() {
        return is_sterilization;
    }

    public String getHair_type() {
        return hair_type;
    }

    public String getNote() {
        return note;
    }

    public String getResettlement() {
        return resettlement;
    }

    public String getPhone() {
        return phone;
    }

    public String getEmail() {
        return email;
    }

    public String getChildre_anlong() {
        return childre_anlong;
    }

    public String getAnimal_anlong() {
        return animal_anlong;
    }

    public String getBodyweight() {
        return bodyweight;
    }

    public String getImage_name() {
        return image_name;
    }

    public String getImage_file() {
        return image_file;
    }

    public String getImageFileThumb() {

        return image_file.split("[.]")[0]+"_248x350"+".jpg";
    }

    public String getPub_date() {
        return pub_date;
    }

    private String name;
    private String sex;
    private String type;
    private String build;
    private String age;
    private String variety;
    private String reason;
    private String accept_num;
    private String chip_num;
    private String is_sterilization;
    private String hair_type;
    private String note;
    private String resettlement;
    private String phone;
    private String email;
    private String childre_anlong;
    private String animal_anlong;
    private String bodyweight;
    private String image_name;
    private String image_file;
    private String pub_date;
}
